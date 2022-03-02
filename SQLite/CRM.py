import dealDB
connection = dealDB.connect_sql("CRM.db")
sql = """ CREATE TABLE IF NOT EXISTS CRM(
    FirstName TEXT,
    LastName TEXT,
    TelNum INT,
    Email TEXT,
    Age INT,
    IsMember BOOL
    );
"""
dealDB.db_change(connection,sql)
category_list = ["first name","last name","phone number","email","age","is he/she a club member? (yes/no)"]

def insert_into_SQL (category_list):
    for category in range (len(category_list)):
        if category == 5:
            category_list[category] = input(f"{category_list[category]}").lower().replace(" ","")
            if category_list[category]=="yes":
                category_list[category]="True"
            else:
                category_list[category] = "False"
        else:
            category_list[category] = input(f"please enter customer's {category_list[category]}")
    sql = f"""INSERT INTO CRM VALUES ("{category_list[0]}","{category_list[1]}",{category_list[2]},"{category_list[3]}",{category_list[4]},"{category_list[5]}");"""
    dealDB.db_change(connection, sql)

def delete_from_SQL (first_name,email):
    sql = f""" DELETE FROM CRM WHERE FirstName="{first_name}" AND Email="{email}" """
    dealDB.db_change(connection, sql)

def return_full_SQL():
    sql = """ SELECT * FROM CRM; """
    return dealDB.db_query(connection,sql)

exit = "true"
while exit != "exit":
    action = input("please choose between the following actions: 1 - Add New Customer, 2 - Delete Customer, 3 - Show All Customers").lower().replace(" ","")
    if action == "1" or action == "addnewcustomer":
        insert_into_SQL(category_list)
    elif action == "2" or action == "deletecustomer":
        first_name=input("please enter the first name of the customer you would like to remove")
        email = input("please enter the email of the customer you would like to remove")
        delete_from_SQL(first_name,email)
    elif action == "3" or action == "showallcustomers":
        rows = return_full_SQL()
        for row in rows:
            print(row)
    else:
        print("action was not found")
    exit = input("press enter if u wanna keep going else, write exit").lower().replace(" ","")