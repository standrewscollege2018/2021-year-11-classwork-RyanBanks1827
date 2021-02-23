import random
import time
randvalue=0
bubu=[]

while(True):
    rar = random.getrandbits(randvalue)
    time.sleep(0.1)
    bubu.append(rar)
    print(bubu)

    if randvalue==0:
        randvalue=1
    elif randvalue==1:
        randvalue=0
    bubu=[]


