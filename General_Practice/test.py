#task 1
def append_value(dict_obj, key, value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = value

import string
str1 = input('enter a string')
dict = {}
low = 0
up = 0
num = 0
punc = 0
space = 0
for i in range (len(str1)):
    index = str1[i]
    if (index.islower()):
        low+=1
    elif (index.isupper()):
        up+=1
    elif (index.isnumeric()):
        num+=1
    elif (index.isspace()):
        space+=1
    else:
        punc+=1
append_value(dict, 'lower', low)
append_value(dict, 'upper', up)
append_value(dict, 'numeral', num)
append_value(dict, 'space', space)
append_value(dict, 'punctuation', punc)
print (dict)

#task 2
alarm_dict = {114: 'נחל עוז', 102: 'כיסופים', 113: 'כרמיה', 148: 'אשקלון', 168: 'אזור תעשייה הדרומי אשקלון', 163: 'נתיב העשרה', 123: 'זיקים', 94: 'מבקיעים', 89: 'מטווח ניר עם', 88: 'אשדוד - אזור תעשייה צפוני'}
def Sum(alarm_dict):
    sum = 0
    for i in alarm_dict.keys():
        sum +=i
    print ("The Total Alarms is",sum)
Sum(alarm_dict)

def TopFive(a1):
    a2 = reversed(sorted(a1.keys()))
    x=0
    for i in a2:
        if x<5:
            print(i,"Rockets in", a1[i])
        x+=1
TopFive(alarm_dict)