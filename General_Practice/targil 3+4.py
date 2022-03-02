# תרגיל 3
temp = (input('please enter the temp in Fahrenheit (with "F" at the ending) or in Celsius (with "C" at the ending) in order to get the temp in the other unit')).lower().replace(" ","")
len = temp.__len__()
temp_in_num = float(temp[:len-1])
f = (temp_in_num*9+32*5)/5
c = (temp_in_num * 5 - 160) / 9
if temp[len-1] == 'f':
        print (f"{c}C")
if temp[len-1] == 'c':
        print (f"{f}F")

#תרגיל 4
total_income = 0
income = []
for i in range (7):
    income.append(int(input(f"please enter day number {i+1} income -  ")))
    total_income += income[i]
print ("best selling day was day number ",income.index(max(income))+1)
print ("worst selling day was day number ",income.index(min(income))+1)
print ("total income is - ",total_income)

# #מהעבודות כיתה:
# #יוצר סיסמאות
import random
import string
exit = 0
while (exit != "exit"):
    num = int(input("enter the lenght of the password"))
    if num>4:
        char = (string.ascii_letters).replace(" ","").lower()
        password = ''.join(random.choice(char) for i in range(num-2))
        first = string.ascii_letters.upper()
        first = ''.join(random.choice(first) for i in range(1))
        sign = string.punctuation
        sign = ''.join(random.choice(sign) for i in range(1))
        print("Random password is:", (first) + password + (sign))
    else:
        print("error")
    exit = input("press enter if u wanna keep running the simulator, else write exit").lower().replace(" ","")

# #אבן נייר ומספריים
exit = 0
while (exit != "exit"):
    rps = input("please choose between rock/paper/scissors").lower().replace(" ","")
    computer = [("rock"),("paper"),("scissors")]
    ran = ''.join(random.choice(computer) for i in range(1))
    print ("computer chose:",ran)
    if (ran == rps):
       print ("draw")
    elif (ran == "rock" and rps=="scissors"):
        print ('you lost')
    elif (ran == "scissors" and rps=="rock"):
        print ('you won')
    elif (ran == "paper" and rps == "scissors"):
        print ('you won')
    elif (ran == "scissors" and rps == "paper"):
        print ('you lost')
    elif (ran == "paper" and rps == "rock"):
        print ('you lost')
    elif (ran == "rock" and rps == "paper"):
        print ("you won")
    else:
        print ("that was not an option!")
    exit = input("press enter if u wanna keep playing, else write exit").lower().replace(" ","")