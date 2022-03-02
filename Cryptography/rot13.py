import string
file = open("text","r")
file_text = file.read()
def rot13(file_text):
    L1 = string.ascii_uppercase[:13]
    L2 = string.ascii_uppercase[13:]
    l1 = string.ascii_lowercase[13:]
    l2 = string.ascii_lowercase[:13]
    str1 = ""
    for ch in file_text:
        for i in range(len(l2)):
            if ch == L1[i]:
                str1+=L2[i]
                break
            elif ch == L2[i]:
                str1+=L1[i]
                break
            elif ch == l1[i]:
                str1+=l2[i]
                break
            elif ch == l2[i]:
                str1+=l1[i]
                break
            elif ch.isnumeric() or ch.isspace() or ch in string.punctuation:
                str1+=ch
                break
    file = open(f"""{input("enter new file name")}""","w")
    file.write(str1)
    file.close()
rot13(file_text)