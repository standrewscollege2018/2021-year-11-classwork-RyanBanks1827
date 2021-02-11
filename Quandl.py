import quandl
import matplotlib.pyplot as plt
import time
while(True):
    time.sleep(0.1)
    mydata = quandl.get("RATEINF/INFLATION_NZL")


