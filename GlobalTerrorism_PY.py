from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
%matplotlib inline


filename = r'C:/Users/kenny/Desktop/global_terrorism/global_terrorism.csv'


df = pd.read_csv(filename, 
                 dtype={'latitude':'float', 
                        'longitude':'float', 
                        'iyear':'float', 
                        'nkill':'float'},
                 low_memory=False, 
                 encoding='latin-1')
				 
df = df.fillna(0)


for i in range(1970,2017):
    plt.clf()
    
    no_kill_alpha = 0.6
    alpha = 0.3
    
    category = [3,6,24,40,80]
    marker_color = [(1,0.5,0,no_kill_alpha), (1,0.2,0,alpha), (1,0.07,0,alpha), (1,0,0,0.4), (1,0,0,0.4)]
    marker_edge_color = [(1,0.5,0), (1,0.2,0), (1,0.07,0), (1,0,0), (1,0,0)]
    ocean_color = (0.14, 0.12, 0.2)
    continent_color = (0.25, 0.25, 0.29)
    
    map = Basemap(projection='cyl', resolution = 'l')

    plt.figure(figsize=(48,22))

    map.drawmapboundary(fill_color=ocean_color)
    map.fillcontinents(color=continent_color)
    map.drawcountries(color=ocean_color, linewidth = 0.2)
    
    df1 = df.loc[(df['iyear'] == i)]

    list_nkill = df1.nkill.values
    x_list = df1.longitude.values 
    y_list = df1.latitude.values
    
    for x, y, deaths in zip(x_list, y_list, list_nkill):
        
        if deaths == 0:
            msize = category[0]
            mcolor = marker_color[0]
            medge = marker_edge_color[0]
        elif deaths > 0 and deaths < 50:
            msize = category[1]
            mcolor = marker_color[1]
            medge = marker_edge_color[1]
        elif deaths >= 50 and deaths < 150:
            msize = category[2]
            mcolor = marker_color[2]
            medge = marker_edge_color[2]
        elif deaths >= 150 and deaths < 500:
            msize = category[3]
            mcolor = marker_color[3]
            medge = marker_edge_color[3]
        else:
            msize = category[4]
            mcolor = marker_color[4]
            medge = marker_edge_color[4]
            
        if(x != 0 and y != 0):
            map.plot(x,y, linestyle='none', marker="o", markeredgecolor=medge, markeredgewidth=0.5, markersize=msize, c=mcolor)

    
    plt.annotate(i, xy=(0.01,0.02), xycoords='axes fraction', size=50, color='white')

    name = str(i)
    extension = ".png"
    path = "C:/Users/kenny/Desktop/global_terrorism/img/"
    
    filename = path + name + extension
    

    plt.savefig(filename)
    plt.show()

