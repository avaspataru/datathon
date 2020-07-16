import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_name = "./museums.xlsx"
dfs = pd.read_excel(file_name, sheet_name="Monthly")

month_names = ["April","May","June","July","August","September","October","November","December","January","February","March"]
month_nums = [4,5,6,7,8,9,10,11,12,1,2,3]
ordered_month_names = [ month_names[ (i+9) % 12] for i in range(0,12) ]

years = [2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]


museum_names = []
museum_ids = []
current_museum = -1

# dict [ (musum id,year num,month num) ] = number of visitors
dict = {}

for (i,r) in dfs.iterrows():
    if i < 18:  # skip headers & total
        continue

    if r[1] == "2004/2005": # new museum
        current_museum += 1
        museum_names.append(r[0])
        museum_ids.append(current_museum)
        continue

    if r[0] in month_names:
        month_num = month_nums[ month_names.index(r[0]) ]

        for j in range(1, 17):
            year = j-1
            key = (current_museum, year, month_num)
            if not isinstance(r[j],int):
                 continue
            dict[key] = int(r[j])


to_plot_2012 = []
to_plot_2011 = []
to_plot_2013 = []
for m in range(1,13):
    k = (0,8,m)
    to_plot_2012.append(dict[k])
    k = (0,7,m)
    to_plot_2011.append(dict[k])
    k = (0,9,m)
    to_plot_2013.append(dict[k])


plt.plot(range(1,13), to_plot_2012, label ="2012")
plt.plot(range(1,13), to_plot_2011, label = "2011")
plt.plot(range(1,13), to_plot_2013, label = "2013")
plt.xticks(np.arange(1,13,1), ordered_month_names, rotation=90)
plt.title("British museum visits by month and year")
plt.legend()
plt.show()
