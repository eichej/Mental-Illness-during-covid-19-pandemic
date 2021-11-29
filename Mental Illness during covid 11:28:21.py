#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:12:40 2021

@author: josephweichenbaum
"""

import matplotlib.pyplot as plt
import datetime
year = 2019,2020,2021
population = 8.1,36.1,27.8 

plt.scatter(year, population)

x = [2019,2020,2021]
y = [8.1,34.5,29.3]
plt.plot(x,y)
plt.show()