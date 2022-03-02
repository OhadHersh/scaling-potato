import sqlite3
def connect_sql(dbname):
    connection = sqlite3.connect(dbname)
    return connection
def db_change(connection,sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    print("SQL executed successfully")
def db_query(connection,sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows