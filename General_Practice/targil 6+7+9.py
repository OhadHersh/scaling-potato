#בתרגילים 6 ו7 החשבתי את הרווחים כתוים מפני שלא ביקשו לבטל אותם
#תרגיל 6
s = input('enter a sentence')
print (s[0]+s[1:].replace(s[0],'e'))

#תרגיל 7
s1 = input('enter another sentence')
s2 = int(len(s1)//2)
print (s1[:s2].lower()+s1[s2:].upper())

#תרגיל 9
x = input('please input a sentence')
x = x.lower().replace(" ","")
if  x[: int(len(x)/2)]==("".join(reversed(x[len(x) - int(len(x)/2):]))):
    print ('OK')
else:
    print ('NOT')