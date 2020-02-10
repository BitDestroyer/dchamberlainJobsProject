class Jobs:


import urllib
import json
from urllib import request

# including the url and variable decleration
url = "https://jobs.github.com/positions.json?&page=0"
listOfJobs = []
results = False


# this function is to open a new file for storing data
def new_file():
    file = open("List_Of_Jobs", "w+")
    read_list(file)
    file.close()


# this will read off the list of data in loop manor
def read_list(file):
    for i in listOfJobs:
        i = i + " " + "\n"
        file.write(i)


def word_check():
    for i in listOfJobs:
        if i == "job":
            results = True


# this function is to grab the data from the url and make it a string
def json_converter():
    return json.dumps(urllib.request.urlopen(url).read().decode())


def test_job_list_length():
    assert len(listOfJobs) >= 100


def test_List_Of_Jobs_contain():
    word_check()
    assert results == True


# a classic main to run all the functions
if __name__ == '__main__':
    listOfJobs = [json_converter()]
    new_file()
    # this print is for my own sanity to make sure the program works
    print(listOfJobs)
