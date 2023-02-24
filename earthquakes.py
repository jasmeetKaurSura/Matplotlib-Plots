# import all libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import datetime

# import and transform data
df= pd.DataFrame
df = pd.read_csv('data.csv')
df.drop_duplicates()
df[('date')]= pd.to_datetime(df['date'])
df.sort_values




fig, ax = plt.subplots(figsize=(5, 3.7), layout='constrained')

ax.set_xlim([2007,2024])

# produce arrays for plot
fig.suptitle("Earthquakes Globally 2008-2022", size=14)
data = {'a': df['date'].dt.year,
        'c': df['magnitude'],
        'd': df['depth'],
        'b': df['magnitude']}
    
scatter= ax.scatter('a', 'b', c='c', s='d', data=data, marker = 'o', alpha= 0.5)
# produce a legends
handles, labels = scatter.legend_elements(prop="colors", alpha=0.5)
legend = ax.legend(handles, labels,loc="upper right", title="magnitude" )
ax.add_artist(legend)
handles1, labels1 = scatter.legend_elements(prop="sizes", alpha=0.5)
legend1 = ax.legend(handles1, labels1,loc="center right", title="depth" )

# produce a axis titles
ax.set_xlabel('Year')
ax.set_ylabel('Magnitude')
plt.show()