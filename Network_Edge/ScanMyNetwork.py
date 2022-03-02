import GetIP
import os
import threading
import string
def ScanNetworkEdge(i):
    count_dot = 0
    net_id = ""
    for code in GetIP.GetNetworkId():
        if count_dot == 3:
            break
        if code == ".":
            count_dot+=1
        net_id += code
    if i.isnumeric():
        new_command = os.popen(f"ping {net_id + i}").read()
        if "(0% loss)" in new_command and "Destination host unreachable" not in new_command:
            print(f"IP {net_id + i} is UP")
    return net_id
net_id = ScanNetworkEdge('a')[:len(ScanNetworkEdge('a'))-1]
print (f"Your IP is ---> {GetIP.GetNetworkId()} \nYour network ID is ---> {net_id} \nStart scanning your network... \nYour network found:")
for i in range(256):
    th1 = threading.Thread(target=ScanNetworkEdge,args=(f"{i}",))
    th1.start()