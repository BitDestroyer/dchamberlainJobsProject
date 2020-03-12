import sqlite3
import xml.etree.ElementTree as ET
from opencage.geocoder import OpenCageGeocode


def open_db(filename: str):
    connection = sqlite3.connect(filename)
    return connection


def setup_db(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS jobs(title TEXT, description TEXT, location TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS locals(location TEXT unique, lat REAL, lng REAL)')


def store_in_db(cursor, title, location, description):
    cursor.execute('INSERT INTO jobs (title, location, description) VALUES (?, ?, ?)',
                   (str(title), str(location), str(description),))
    cursor.execute('SELECT location FROM locals WHERE location = "{}"'.format(location))
    existing_locals = cursor.fetchall()
    if len(existing_locals) == 0:
        key = 'af6bc3fce8f545e59cf087959211d13d'
        geo_coder = OpenCageGeocode(key)

        lat_lng = geo_coder.geocode(location)
        if len(lat_lng) > 0:
            lat = lat_lng[0]['geometry']['lat']
            lng = lat_lng[0]['geometry']['lng']
        else:
            lat = 0
            lng = 0

        cursor.execute('INSERT INTO locals (location, lat, lng) VALUES (?, ?, ?)',
                       (str(location), float(lat), float(lng)))


def parse_xml(cursor, xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    for item in root.findall('./channel/item'):
        title = item.find('./title')
        location = str(title.text).rpartition('(')[-1].strip(')')

        description = item.find('./description')
        store_in_db(cursor, title.text, location, description.text)


con = open_db("jobs.db")
cur = con.cursor()
setup_db(cur)

parse_xml(cur, 'list_of_jobs.xml')

con.commit()
