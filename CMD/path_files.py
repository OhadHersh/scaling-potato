import os
path = input("which path would you like to use")
def FileExplorer (path):
    DIR = os.listdir(path)
    if DIR == []:
        print(f"path {path} is empty")
    else:
        print(f"chosen path is: {path}\nfiles that are in this path: ")
        for i in DIR:
            print (f"{(DIR.index(i)+1)}. {i}")
FileExplorer(path)