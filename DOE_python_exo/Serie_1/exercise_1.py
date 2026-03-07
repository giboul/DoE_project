
import os, sys, os.path, shutil
import matplotlib as mpl

import xlrd, openpyxl
import hashlib
import pweave

mode_serv = False
for param in sys.argv[1:]:
    if param[:len("serv")]=="serv" and param[len("serv")] == "=":
        mode_serv = param[len("serv")+1:] in "1 y Y yes Yes YES"
#if not mode_serv:
#    mpl.use('TkAgg')
#else:
#    mpl.use('Agg')
if mode_serv:
    mpl.use('Agg')
try:
    import appnope
    appnope.nope()    # stop the apple power nap
except ImportError:
    pass

import pandas
from math import pi
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import numpy as np
from numpy.random import rand
from pylab import pcolor, show, colorbar, xticks, yticks, pcolormesh, imshow
from random import gauss
from scipy.interpolate import interp2d
import threading, multiprocessing, time
from decimal import Decimal

from scipy.optimize import curve_fit
mpl.rc('text', usetex=True)
#plt.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r"\usepackage{amsmath} \usepackage{graphicx} \usepackage{nicefrac} \usepackage{xcolor}")

import scipy as sp
import subprocess
import datetime
from matplotlib.ticker import PercentFormatter




Excel_wb=pandas.ExcelFile("data_publication.xlsx")
Data=pandas.read_excel(Excel_wb,"Data")
country=pandas.read_excel(Excel_wb,"Metadata - Countries")
population=pandas.read_excel(Excel_wb,"population",header=3)
population=population[2:]
print(Data)
print(len(Data))
print(population[2:])
print(pandas.merge(population,Data,how="left",on="Country")) # if a value doesnt exit, it places a Nan
Merged_file=pandas.merge(population,Data,how="left",on="Country")
Merged_file["Code"].astype("category")
Merged_file["Region"].astype("string")
# Merged_file["Region"].astype("category")
print(Merged_file["Region"])
Merged_file["Level"].astype("category")
ax=Merged_file.plot(x="Level", y="publication 2018",marker=".",linestyle="")
# plt.xscale("log")
plt.yscale("log")


Table2=Merged_file.groupby("Region").aggregate(func=sum).reset_index()
print(Table2)
print(np.divide(Table2["publication 2018"].values,min(Table2["publication 2018"].values)))

si=np.divide(Table2["publication 2018"].values,min(Table2["publication 2018"].values))

Table2["Region"].astype("category")
Table2.plot.scatter(x="Region", y="2018", s=si*10)

print(Merged_file.aggregate(func=sum)["publication 2000":"publication 2018"].reset_index().rename(columns={0:"A"})) #omg ça marche
print(Merged_file.aggregate(func=sum)["publication 2000":"publication 2018"].reset_index().rename(columns={0:"A"}).dtypes) #omg ça marche
Table3=Merged_file.aggregate(func=sum)["publication 2000":"publication 2018"].reset_index().rename(columns={0:"A"})
Table4=Table3.astype({"A":"float"})
print(Table4.dtypes)
plt.figure(3)
Table4.boxplot(column="A")




#sort DataFrame by publication 2000 descending
df = Merged_file.sort_values(by='publication 2000', ascending=False).reset_index()

#add column to display cumulative percentage
df['cumperc2000'] = df['publication 2000'].cumsum()/df['publication 2000'].sum()*100
print(df["publication 2000"])
#define aesthetics for plot
color1 = 'steelblue'
color2 = 'red'
line_size = 4

#create basic bar plot
fig, ax = plt.subplots()
ax.bar(df.index, df['publication 2000'], color=color1)

#add cumulative percentage line to plot
ax2 = ax.twinx()
ax2.plot(df.index, df['cumperc2000'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

#specify axis colors
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)


df = Merged_file.sort_values(by='publication 2018', ascending=False).reset_index()

#add column to display cumulative percentage
df['cumperc2018'] = df['publication 2018'].cumsum()/df['publication 2018'].sum()*100
print(df["publication 2018"])
#define aesthetics for plot
color1 = 'steelblue'
color2 = 'red'
line_size = 4

#create basic bar plot
fig, ax = plt.subplots()
ax.bar(df.index, df['publication 2018'], color=color1)

#add cumulative percentage line to plot
ax2 = ax.twinx()
ax2.plot(df.index, df['cumperc2018'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

#specify axis colors
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)






#sort DataFrame by publication 2000 descending
df = Table2.sort_values(by='publication 2000', ascending=False).reset_index()

#add column to display cumulative percentage
df['cumperc2000'] = df['publication 2000'].cumsum()/df['publication 2000'].sum()*100
print(df["publication 2000"])
#define aesthetics for plot
color1 = 'steelblue'
color2 = 'red'
line_size = 4

#create basic bar plot
fig, ax = plt.subplots()
ax.bar(df.index, df['publication 2000'], color=color1)

#add cumulative percentage line to plot
ax2 = ax.twinx()
ax2.plot(df.index, df['cumperc2000'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

#specify axis colors
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)


df = Table2.sort_values(by='publication 2018', ascending=False).reset_index()

#add column to display cumulative percentage
df['cumperc2018'] = df['publication 2018'].cumsum()/df['publication 2018'].sum()*100
print(df["publication 2018"])
#define aesthetics for plot
color1 = 'steelblue'
color2 = 'red'
line_size = 4

#create basic bar plot
fig, ax = plt.subplots()
ax.bar(df.index, df['publication 2018'], color=color1)

#add cumulative percentage line to plot
ax2 = ax.twinx()
ax2.plot(df.index, df['cumperc2018'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

#specify axis colors
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)


plt.show()

