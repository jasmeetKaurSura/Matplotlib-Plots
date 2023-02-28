import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors

#load data
df= pd.DataFrame
df = pd.read_csv('TravelCanada.csv')
#create figure
fig, ax = plt.subplots(figsize=(10, 10), layout='constrained' )
fig.suptitle("Travel by Canadian residents by trip purpose", size=14)


#create artis for animation
artists = []

#find values for different containers
column_names = list(df.columns.values)
column_names.remove('Main trip purpose')

#add different containers to artists
for i in range(1,8,1):
    data = df.loc[i,'Q1 2019':'Q3 2022']
    container = ax.bar(column_names, data)
    ax.legend(df["Main trip purpose"], loc='upper right', title= 'Main trip purpose')
    artists.append(container)

#labeling the x and y axis
ax.set_ylabel("Number of trips (X 1000)")
ax.set_xlabel("Reference period")
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right') 

ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=1200)


# To save the animation using Pillow as a gif
ani.save('myanimation.gif') 
writer = animation.PillowWriter(fps=0.1)
ani.save('scatter.gif', writer=writer)
plt.show()

