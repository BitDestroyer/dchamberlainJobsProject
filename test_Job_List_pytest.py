import Job_List


def test_job_list_length():
    assert len(Job_List.listOfJobs) >= 100


def test_List_Of_Jobs_contain():
    Job_List.word_check()
    assert Job_List.results == True