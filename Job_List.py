import requests


class Jobs:

    # this function is to open a new file for storing data
    def __init__(self):
        self.url = ["https://jobs.github.com/positions", "https://jobs.github.com/positions?page=2",
                    "https://jobs.github.com/positions?page=4",
                    "https://jobs.github.com/positions?page=5"]
        self.listOfJobs = []
        self.results = False

    def new_file(self):
        self.file = open("List_Of_Jobs", "w+")
        for i in self.listOfJobs:
            self.write_list(list.append(i.text))
        self.file.close()

    # this will read off the list of data in loop manor
    def write_list(self):
        for j in self.url:
            print(j)
            response = requests.get(j)
            if response == 200:
                newJobList.webpages = requests.get(j).json()
                newJobList.listOfJobs.append(newJobList.webpages)
                newJobList.new_file()
            else:
                print("no response from github\n")

    def word_check(self):
        for i in newJobList.listOfJobs:
            if i == "job":
                results = True


# a classic main to run all the functions
if __name__ == '__main__':
    newJobList = Jobs()
    webpages = []
    listOfJobs = []
    newJobList.write_list()
    # this print is for my own sanity to make sure the program works
    print("end of sprint 1")
