import sqlite3
def connect_sqlite3(dbname):
    connection = sqlite3.connect(dbname)
    return connection
def db_change(connection,sql):
    cursor = connection.cursor()
    cursor.execute(sql) # execute the SQl command
    connection.commit() #DO the command
    print("SQL executed succesfully")
def db_query(connection,sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
def WhatDoIDo():
    text = input("Have u faced a sick person? (yes/no)").lower()
    if "yes" in text:
        text = input("Are you vaccinated? (yes/no)").lower()
        if "yes" in text:
            text = input("Please perform an antigen test...\nAre you positive or negative?").lower()
            if "positive" in text:
                text = input("Please perform a PCR test...\nAre you positive or negative?").lower()
                if "positive" in text:
                    return "10 days quarantine"
            return "No need of quarantine"
        text = input("Please perform a PCR test...\nAre you positive or negative?").lower()
        if "positive" in text:
            return "10 days quarantine"
        return "7 days quarantine"
    return "No need of quarantine"
connection = connect_sqlite3("Corona.db")

sql = """ CREATE TABLE IF NOT EXISTS Corona(
    ClientNum INT,
    FirstName TEXT,
    LastName TEXT,
    ID INT,
    Command TEXT
    );
"""
db_change(connection,sql)
count = 1
text = input("Would you like to insert a client?").lower()
while "yes" in text:
    firstname = input("What's your first name?")
    lastname = input("What's your last name?")
    ID = input("What's your ID?")
    command = WhatDoIDo()
    sql = f"""INSERT INTO Corona VALUES ({count},"{firstname}","{lastname}",{ID},"{command}");"""
    db_change(connection, sql)
    count+=1
    text = input("Would you like to insert another client?").lower()
sql = """SELECT * FROM Corona"""
rows = db_query(connection,sql)
for row in rows:
    print(row)