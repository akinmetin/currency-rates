import timeit

# checking function execution time to determine sharp remaining time
mysetup = "import datetime"

mycode = """
def get_remaining_time():
    currentDT = datetime.datetime.now()
    hours = currentDT.hour
    minutes = currentDT.minute
    seconds = currentDT.second

    # start to calculate remaining sleeping time in seconds
    remain = (24 - hours)*3600 + (60 - minutes)*60 + seconds
    return remain
"""

if __name__ == "__main__":
    print(timeit.timeit(setup=mysetup, stmt=mycode, number=10000))