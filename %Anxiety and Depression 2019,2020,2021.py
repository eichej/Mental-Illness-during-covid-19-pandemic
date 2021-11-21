#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:19:57 2021

@author: josephweichenbaum
"""

import matplotlib.pyplot as plt
import datetime
year = 2019,2020,2021
population = 8.1,36.1,27.8 

plt.scatter(year, population)

x = [2019,2020,2021]
y = [10.8,38.9,34]
plt.plot(x,y)
plt.show()