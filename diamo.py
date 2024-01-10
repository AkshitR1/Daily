import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

file = "C:/Users/rtran/OneDrive/Desktop/Py(VS)/daily/diamond/diamonds.csv"
ds = pd.read_csv(file , index_col=0)
ds.shape

ds.head()

ds.query('cut == "Good"')

cost = ds.query("price >= 16000")
figure = px.bar(cost, x=cost["price"], y = cost["cut"], title="cost n cut")
figure.show()

cost = ds.query("carat >= 1")
figure = px.bar(cost, x=cost["cut"], y = cost["carat"], title="cost n carat", color='cut')

figure.update_layout(
    xaxis_title='Cut',  
    yaxis_title='Carat',  
    width=800, 
    height=600,
    bargap=0.2,
    coloraxis_colorbar=dict(
        title='Cut Types',  
    )
)

figure.show()