import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

file = "NSEI .csv"
ds = pd.read_csv(file)
ds.shape

ds.describe()

ds.query('Open>= 15200')

cost = ds.query("Low >= 15000")
figure = px.bar(cost, x=cost["Date"], y = cost["Low"], title="Highest Lows")
figure.show()

cost = ds.query("Low <= 3000")
figure = px.bar(cost, x=cost["Date"], y = cost["Low"], title="Lowest Lows", color_continuous_scale='Viridis',  height=600, width=1200)
figure.update_layout(
    xaxis_title='Date',
    yaxis_title='Lowest Price',
    bargap=0.05,  )
figure.show()

cost = ds.query("Close <= 3000")
figure = px.bar(cost, x=cost["Date"], y = cost["Low"], title="Lowest Close")
figure.show()

vol = ds.query("Volume >=1000000")
figure = px.bar(vol, x=vol["Date"], y = vol["Volume"], title="Most trades")
figure.show()
