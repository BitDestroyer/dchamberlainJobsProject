# dchamberlainJobsProject
First Sprint
Douglas Chamberlain

install and run directions:
please pip install opencage
as well pip install plotly

pystests should be independantly runnable test, to run the independant test right click on the individual tests with function
names starting with the word "test_" to run tests. You will need pytest installed! For anything else you can just run the file!

The project I made is designed to retrieve data from stack overflow. The program will receive a list of jobs
and then it will automatically sift through the data of jobs retrieved, and it will store the titles, descriptions, and locations
into a database. From this database it will use the locations to display a map that has plotted the locations of the jobs.

The plotted map will pop up automatically on a webpage so please have internet access.

** Important Run Instructions

To run the program please first run the Joblist.py file! it collects the XML data from Stack overflow.
Next please run Job_DB, this task will run for several minutes please be patients it will sift through 1000 jobs, to
collect their coordinates and to sort out duplicate locations. All that remains once Job_DB has completed its task is
to run job_plotter which will access a webpage to display all the jobs on a map!