#code that draws bargraph and save the image in a buffere and returns it to client 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import BytesIO

class GraphImages:
    @staticmethod
    def trendGraph(raw_data):
        df = pd.DataFrame(data=raw_data)
        buffer = BytesIO()

        plt.figure(figsize=(12,3))
        plt.plot(df['x'],df['y'],'--b', marker='o')
        plt.ylim(0,100)

        for x,y in zip(df['x'],df['y']):
            label = "{:.2f}".format(y)
            plt.annotate(label, # this is the text
                (x,y), # this is the point to label
                textcoords="offset points", # how to position the text
                xytext=(0,5), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center

        plt.grid(color='#666666', linestyle='--')
        plt.savefig(buffer, transparent = True, bbox_inches = 'tight', format="png")
        plt.close()
        return buffer.getvalue()
    