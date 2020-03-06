import requests
from decouple import config
import datetime
from calendar import monthrange
import psycopg2
import time


def create_db_table():
    con = psycopg2.connect(database=config("DB_NAME"), user=config("DB_USER"),
                           password=config("DB_PASSWORD"),
                           host=config("DB_HOST"), port=config("DB_PORT"))
    cur = con.cursor()
    cur.execute('''CREATE TABLE rates
      (DATE              VARCHAR(10)     NOT NULL,
      CURRENCY           VARCHAR(3)      NOT NULL,
      VALUE              FLOAT           NOT NULL);''')
    con.commit()
    con.close()


def first_run():
    # first create a table in the database
    create_db_table()

    currentDT = datetime.datetime.now()
    year = currentDT.year
    month = currentDT.month

    # find the previous month's number. If current month is the first month,
    # then go to December of the previous year.
    if year != 1:
        month -= 1
    else:
        month = 12
        year -= 1

    # get total number of days in target month.
    total_days = monthrange(year, month)[1]

    # create database connection
    con = psycopg2.connect(database=config("DB_NAME"), user=config("DB_USER"),
                           password=config("DB_PASSWORD"),
                           host=config("DB_HOST"), port=config("DB_PORT"))
    cur = con.cursor()

    # get entire month's data.
    # http://data.fixer.io/api/YYYY-MM-DD?access_key=.....
    for x in range(1, total_days + 1):
        date = "{}/{}/{}".format(x, month, year)
        url = "http://data.fixer.io/api/%s-%s-%s?access_key=%s" % \
            (year, str(month).zfill(2), str(x).zfill(2), str(config("API_KEY")))
        print(url)

        response = requests.get(url)
        data = response.json()["rates"]

        for attr in data.keys():
            cur.execute("INSERT INTO rates (DATE,CURRENCY,VALUE) \
                VALUES (%s, %s, %s)", (date, str(attr), data[attr]))

    # commit the waiting insert queries and close the connection.
    con.commit()
    con.close()
    insert_into_db()


def check_db_table_exits():
    con = psycopg2.connect(database=config("DB_NAME"), user=config("DB_USER"),
                           password=config("DB_PASSWORD"),
                           host=config("DB_HOST"), port=config("DB_PORT"))
    cur = con.cursor()
    cur.execute("select * from information_schema.tables where table_name=%s", ('rates',))
    if bool(cur.rowcount):
        con.close()
    else:
        con.close()
        first_run()


def insert_into_db():
    # get current date
    currentDT = datetime.datetime.now()
    year = currentDT.year
    month = currentDT.month
    day = currentDT.day
    date = "{}/{}/{}".format(day, month, year)

    # create database connection
    con = psycopg2.connect(database=config("DB_NAME"), user=config("DB_USER"),
                           password=config("DB_PASSWORD"),
                           host=config("DB_HOST"), port=config("DB_PORT"))
    cur = con.cursor()

    # get currency json data from the api server
    response = requests.get(config("API_ENDPOINT"))
    data = response.json()["rates"]

    for item in data.keys():
        cur.execute("INSERT INTO rates (DATE,CURRENCY,VALUE) \
            VALUES (%s, %s, %s)", (date, item, data[item]))
    # commit the waiting insert queries and close the connection.
    con.commit()
    con.close()


def get_remaining_time():
    currentDT = datetime.datetime.now()
    hours = currentDT.hour
    minutes = currentDT.minute
    seconds = currentDT.second

    # start to calculate remaining sleeping time in seconds
    remain = (24 - hours)*3600 + (60 - minutes)*60 + seconds
    return remain


if __name__ == "__main__":
    # check db table, if doesn't exists then create tables and pull last month's data into the db.
    check_db_table_exits()

    # endless loop, sleep until next morning 9 am. and run again
    while True:
        remain = get_remaining_time()
        print("Sleeping: " + str(remain))
        time.sleep(remain)

        # run daily api request and insert fresh data into db.
        insert_into_db()

# https://fixer.io/quickstart
# https://fixer.io/documentation
# https://www.dataquest.io/blog/python-api-tutorial/

# python get time --> https://tecadmin.net/get-current-date-time-python/
# python postgresql --> https://stackabuse.com/working-with-postgresql-in-python/
# check table if exists --> https://stackoverflow.com/questions/1874113/checking-if-a-postgresql-table-exists-under-python-and-probably-psycopg2
# postgres data types (postgres float) --> https://www.postgresqltutorial.com/postgresql-data-types/
# python get number of days in month --> https://stackoverflow.com/questions/4938429/how-do-we-determine-the-number-of-days-for-a-given-month-in-python