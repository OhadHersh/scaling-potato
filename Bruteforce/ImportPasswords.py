import requests
def Get_Password():
    URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"
    file_content = requests.get(URL)
    list = file_content.text.split("\n")
    return list