#!/usr/bin/env pytho3.9
"""
Created on Sun Jan 15 12:39:53 2023
Joseph Worwor
Bachelor of Atmospheric Science
Najing Univbersity of Information Science and Technology
@author: WORWOR
"""
import pandas as pd                       # Data Analysis
import numpy as np                        # Multi-Dimension Array
import matplotlib.pyplot as plt           # Data Visualization

# Concerning pd.read_csv
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html?highlight=read_csv#pandas.read_csv
main_data = pd.read_csv('C:/Users/drbml/Desktop/IMSA_PYTHON_2023/Day 1/Day 1/part 1/China 753 station monthly data 1951-2011.txt',skiprows=1,header=None)
print(main_data)
info_variable   = ["Station No.","Year","Months","Average Temp","Average Max-Temp",
                   "Average Min-Temp","Average Relative Humidity","Precipitation","Average Wind-Speed","Sunshine","Null"]

# Concerning pandas.DataFrame.columns
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html?highlight=columns#pandas.DataFrame.columns
main_data.columns = info_variable
print(main_data)
# Concerning pandas.DataFrame.drop
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html?highlight=drop#pandas.DataFrame.drop
main_data.drop("Null",axis=1,inplace=True)   # axis1 = x, axis0 = y
print(main_data)
# Set the DataFrame index using existing columns.
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html?highlight=set_index#pandas.DataFrame.set_index
main_data.set_index(["Station No.","Year","Months"],inplace=True)

select_stn  = 58238 #Najing (52765)

# Create an object to more easily perform multi-index slicing.
# https://pandas.pydata.org/docs/reference/api/pandas.IndexSlice.html?highlight=pd%20indexslice
idx = pd.IndexSlice

select_data = main_data.loc[idx[select_stn,1981:2010,6:8],idx["Average Temp"]] 
select_data = select_data/10.0 # to degC
print(select_data)
# Returns a DataFrame with a new level column label, whose innermost layer consists of a pivot index label. Unstack
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html?highlight=unstack
select_data_2d = select_data.unstack(2)
print(select_data_2d)
# pandas.DataFrame.mean
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html?highlight=mean#pandas.DataFrame.mean
interannual = select_data_2d.mean(1)
print(interannual)

# output file
interannual.to_csv("C:/Users/drbml/Desktop/IMSA_PYTHON_2023/Day 1/Day 1/part 1/58238_1981_2010_JJA_prep.txt")

# find line of best fit
# a, b = np.polyfit(range(1981,2011), interannual, 1)

# plot 
plt.scatter(range(1981,2011), interannual, color="b")

plt.title("Station Ave Temp")
plt.xlabel("Years")
plt.ylabel("Temperature")

# Connecting point
#plt.plot(range(1981,2011),interannual)  

# add line of best fit to plot
# plt.plot(range(1981,2011), a*range(1981,2011)+b) 

# More graphy can be find in the link below

# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
