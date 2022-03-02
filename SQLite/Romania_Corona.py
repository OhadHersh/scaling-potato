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
URL = "https://news.google.com/covid19/map?hl=he&mid=%2Fm%2F06c1y&gl=IL&ceid=IL%3Ahe"
content = requests.get(URL)
soup = BeautifulSoup(content.text,"html.parser")
total_vac = soup.find_all(class_="UvMayb")[2].text
yesterday_new_cases = soup.find(class_="tIUMlb").text
total_cases = soup.find(class_="UvMayb").text
full_vac = soup.find_all(class_="UvMayb")[4].text
connection = connect_sql("Romania_corona_stats.db")
sql = """ CREATE TABLE IF NOT EXISTS Romania_corona_stats(
    Total_Vaccines TEXT,
    Yesterday_New_Cases TEXT,
    Total_Cases TEXT,
    Full_Vaccinated TEXT,
    Date TEXT
    );
"""
db_change(connection,sql)
date = str(date.today()).replace("-","/")
sql = f"""INSERT INTO Romania_corona_stats VALUES ("{total_vac}","{yesterday_new_cases}","{total_cases}","{full_vac}","{date}");"""
db_change(connection,sql)