import json
import urllib
from urllib import request

#resp = request.urlopen("https://jobs.github.com/positions.json?page=0").read()
#resp = json.dump(resp)
#print(resp)

url = "https://jobs.github.com/positions.json?&page=0"
data = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data)


listOfJobs = []


def new_file():
    file = open("List Of Jobs", "w+")
    for i in listOfJobs:
        i = i + " "
        file.write(i)
    file.close()


def json_converter():
    sitOfJobs = json.dump()


if __name__ == '__main__':
    new_file()