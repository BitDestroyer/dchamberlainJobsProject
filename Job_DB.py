import Job_List
import sqlite3
from typing import Tuple

def open_db(filename:str)->Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    return db,cursor



def setup_db(cursor:sqlite3.Cursor):

    cursor.execute('''CREATE TABLE IF NOT EXISTS job_title(job_name Text)''')


def job_list(cursor:sqlite3.Cursor):
    true_list = []
    #for i in range(number of jobs()
    # add a job name in a column in the database
    for item in true_list:
       cursor.execute(f'''INSERT INTO job_title(job_name) VALUES(?)''', (str(item),))