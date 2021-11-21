#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:35:46 2021

@author: josephweichenbaum
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
#strings
xlab = "years around covid 19"
ylab = "percentage in survey with anxiety"
year = 2019,2020,2021
population = 8.1,36.1,27.8 
#add title
plt.title(mental anxiety during covid)
plt.scatter(year, population)

x = [2019,2020,2021]
y = [8.1,36.1,27.8]
plt.plot(x,y)
plt.show()
