import os
def GetNetworkId():
    ip = os.popen("wmic NICCONFIG WHERE IPEnabled=true GET IPAddress").read()
    return (ip[52:65])