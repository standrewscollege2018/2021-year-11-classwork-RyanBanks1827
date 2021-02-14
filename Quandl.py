import quandl
import pandas

ElapsedTime = 0
import matplotlib.pyplot as plt
import time

while (True):
    ElapsedTime = ElapsedTime + 1
    # print("Time elapsed={}".format(ElapsedTime))

    YearData = quandl.get("RATEINF/CPI_NZL", authtoken="1Yy_wztTrMMBr6AoCATM", collapse='weekly', column_index='1')
    YearData = str(YearData)
    # YearData2=YearData.strip('Value')
    # NewYear=[int(i) for i in YearData.split() if i.isalpha()]
    YearNew=slice(1, 5)
    print(YearData[YearNew])


    # print(YearData2.split(','))

    time.sleep(100)
