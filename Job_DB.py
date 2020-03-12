import sqlite3
import xml.etree.ElementTree as ET
from opencage.geocoder import OpenCageGeocode


# function designed to operate the opening of a new/reopening of a database
def open_db(filename: str):
    connection = sqlite3.connect(filename)
    return connection


# the setup of the database creates 2 tables, one to contain the job titles along with their descriptions
# as well as their locations. However the second database is designed to intake the jobs locations and their
# coordinates because it is a unique database table which only allows one copy/instance of data at a time
# which is how we will keep duplicate locations from being plotted/saved
def setup_db(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS jobs(title TEXT, description TEXT, location TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS locals(location TEXT unique, lat REAL, lng REAL)')


# this will store the individual jobs into the table by their attributes title/description/location
def store_in_db(cursor, title, location, description):
    cursor.execute('INSERT INTO jobs (title, location, description) VALUES (?, ?, ?)',
                   (str(title), str(location), str(description),))
    cursor.execute('SELECT location FROM locals WHERE location = "{}"'.format(location))

    # this will grab all data in local and determine if there is an existing data or not
    existing_locals = cursor.fetchall()
    # if a data does not exist, it is time to insert it
    if len(existing_locals) == 0:
        key = 'af6bc3fce8f545e59cf087959211d13d'
        geo_coder = OpenCageGeocode(key)

        lat_lng = geo_coder.geocode(location)
        if len(lat_lng) > 0:
            lat = lat_lng[0]['geometry']['lat']
            lng = lat_lng[0]['geometry']['lng']

        # otherwise give no lat or lng
        else:
            lat = 0
            lng = 0

        cursor.execute('INSERT INTO locals (location, lat, lng) VALUES (?, ?, ?)',
                       (str(location), float(lat), float(lng)))


# this the parser that runs through the XML data and finds specifics in each item
def parse_xml(cursor, xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # pick out the items in the xml and pull the job title
    for item in root.findall('./channel/item'):
        title = item.find('./title')

        # this will run through the string backwards because the titles contain the location of the job at the end
        # of the string
        location = str(title.text).rpartition('(')[-1].strip(')')

        # to grab the description of the specified item
        description = item.find('./description')
        store_in_db(cursor, title.text, location, description.text)


con = open_db("jobs.db")
cur = con.cursor()
setup_db(cur)

parse_xml(cur, 'list_of_jobs.xml')

con.commit()
