import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import date
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
URL = "https://corona.mako.co.il/"
content = requests.get(URL)
soup = BeautifulSoup(content.text,"html.parser")
sickpeople = soup.find(class_="stat-total").text
sickhard = soup.find_all(class_="stat-total")[3].text
Rvalue = soup.find_all(class_="stat-total")[1].text
connection = connect_sql("today_corona_info.db")
sql = """ CREATE TABLE IF NOT EXISTS today_corona_info(
    Rvalue FLOAT,
    Sickhard INT,
    Sickpeople INT,
    Date TEXT
    );
"""
db_change(connection,sql)
date = str(date.today()).replace("-","/")
sql = f"""INSERT INTO today_corona_info VALUES ({Rvalue},{sickhard},{sickpeople},"{date}");"""
db_change(connection,sql)