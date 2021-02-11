import quandl
ElapsedTime=0
import matplotlib.pyplot as plt
import time
while(True):
    ElapsedTime=ElapsedTime+1
    print("Time elapsed={}".format(ElapsedTime))

    mydata = quandl.get([ "WIKI/NZD.4"])
    print(mydata)


    time.sleep(0.1)




