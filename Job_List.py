import requests


class Jobs:

    # this function is to open a new file for storing data
    def __init__(self):
        self.url = ["https://stackoverflow.com/jobs/feed"]
        self.listOfJobs = []
        self.results = False

    def save(self):
        if self.listOfJobs:
            with open('list_of_jobs.xml', 'wb') as file:
                for i in self.listOfJobs:
                    file.write(i)

    # this will read off the list of data in loop manor
    def write_list(self):
        for j in self.url:
            print(j)
            response = requests.get(j)
            if response.status_code == 200:
                self.listOfJobs.append(response.content)
            else:
                print("no response from server\n")
        self.save()

    def word_check(self):
        for i in newJobList.listOfJobs:
            if i == "job":
                results = True


# a classic main to run all the functions
if __name__ == '__main__':
    newJobList = Jobs()
    newJobList.write_list()
    # this print is for my own sanity to make sure the program works
    print("end of sprint 1")
