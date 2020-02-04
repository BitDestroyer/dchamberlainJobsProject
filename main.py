import urllib
from urllib import request

# including the url and variable decleration
url = "https://jobs.github.com/positions.json?&page=0"
listOfJobs = []


# this function is to open a new file for storing data
def new_file():
    file = open("List Of Jobs", "w+")
    file.close()


# this will read off the list of data in loop manor
def read_list(file):
    for i in listOfJobs:
        i = i + " " + "\n"
        print(i)
        file.write(i)


# this function is to grab the data from the url and make it a string
def json_converter():
    return str(urllib.request.urlopen(url).read().decode())


# a classic main to run all the functions
if __name__ == '__main__':
    listOfJobs = [json_converter()]
    new_file()
    # this print is for my own sanity to make sure the program works
    print(listOfJobs)
