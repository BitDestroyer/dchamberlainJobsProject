import sqlite3
import xml.etree.ElementTree as ET


def open_db(filename: str):
    connection = sqlite3.connect(filename)
    return connection


def setup_db(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS jobs(title TEXT, description TEXT, location TEXT)')


def store_in_db(cursor, title, location, description):
    cursor.execute('INSERT INTO jobs (title, location, description) VALUES (?, ?, ?)',
                   (str(title), str(location), str(description)))


def parse_xml(cursor, xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # iterate news items
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
