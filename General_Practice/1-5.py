#תרגיל 1
#בסעיף א' תודפס הספרה 1 ובשורה מתחתיה תודפס הספרה 1 שוב
#בסעיף ב' תודפס הספרה 2 ובשורה מתחתיה תודפס הספרה 1
#בסעיף ג' לא יודפס כלום
#בסעיף ד' תודפס הספרה 2 ומתחתיה הספרה 2 פעם נוספת

#תרגיל 2
#B, F,

#תרגיל 3
def squared_numbers(start, stop):
    list = []
    while start <= stop:
        list.append(start**2)
        start += 1
    print (list)

squared_numbers(-3, 3)

#תרגיל 4
#A, C

#תרגיל 5
#תשובה A, הפעולה תדפיס האם מחרוזת נתונה st מכילה תו נתון כלשהו c
def what(st, c):
    return c in st
what('ב','z')
