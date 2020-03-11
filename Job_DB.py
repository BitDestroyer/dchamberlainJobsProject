import Job_List
import sqlite3
from typing import Tuple
import xml.etree.ElementTree as ET


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(filename)
    return connection


def setup_db(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs(title TEXT, description TEXT);''')


def store_in_db(cursor, title, description):
    cursor.execute(f'''INSERT INTO jobs (title, description) VALUES (?, ?)''', (str(title),str(description),))


def parse_xml(cursor, xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # iterate news items
    for item in root.findall('./channel/item'):
        title = item.find('./title')
        description = item.find('./description')
        store_in_db(cursor, title.text, description.text)


con = open_db("jobs.db")
cur = con.cursor()
setup_db(cur)

parse_xml(cur, 'list_of_jobs.xml')

con.commit()
