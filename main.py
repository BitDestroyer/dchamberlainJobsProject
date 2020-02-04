listOfJobs = ["Butt", "Stuff", "butt stuff"]


def new_file():
    file = open("List Of Jobs", "w+")
    for i in listOfJobs:
        i = i + " "
        file.write(i)
    file.close()


if __name__ == '__main__':
    new_file()