import string
import random
import time
import threading
def RandonSign():
    sign = string.punctuation
    sign = ''.join(random.choice(sign) for i in range(1))
    return sign
def AutoWrite(sign,FileName):
    file = open(f"{FileName}.txt","w")
    for i in range(10000):
        file.write(sign)
    time.sleep(1)
def AllInOne(FileName):
    AutoWrite(RandonSign(),FileName)
start = time.perf_counter()
for i in range(10):
    th1 = threading.Thread(target=AllInOne, args=(f"file{i+1}", ))
    th1.start()
    # AllInOne(f"file{i+1}")
th1.join()
stop = time.perf_counter()
print(f"Cycle time of all  : {stop-start}")
#cycle time without threading: 10.2163822 sec
#Cycle time with threading: 1.0535244 sec