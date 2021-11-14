# -*- coding: utf-8 -*-
import pandas as pd

import matplotlib.pyplot as plt
import os
os.chdir/Users/mypath').xlsx 

df = pd.read.xls)'\\Users\\josephweichenbaum\\desktop\\mentalillness.xls' 
                    
#create a scatter plot with x axis = progressive dates during covid pandemic,
x = df ['time frame']
y1 = df ['% adults w anxiety']
y2 = df ['% adults w depression']
y3 = df ['% adults w anxiety or depression']

plt.plot(x,y1,label = "% adults w anxiety")
plt.plot(x,y2,label = "% adults w depression")
plt.plot(x,y1,label = "% adults w anxiety or depression")

plt.show()




