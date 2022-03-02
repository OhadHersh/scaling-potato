import rot13
file = open("Data.txt","r")
file_text = file.read()
rot13.rot13(file_text)