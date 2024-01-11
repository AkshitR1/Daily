import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

stats = pd.read_csv("daily\Virat_Kohli.csv")
print(stats.head())
print(stats.tail())

print(stats["Runs"].sum())
print(stats["Runs"].mean())
print(stats["Runs"].max())
print(stats["Runs"].min())
print(stats["Runs"].median())


Strike_R = stats.query("SR >=140")
print(Strike_R)

dismissal_type = stats.query("Dismissal == 'not out'")
print(dismissal_type)

matches = stats.index
figure = px.line(stats, x=matches, y="Runs", 
                 title='Runs Scored by Virat Kohli Between 18-Aug-08 - 22-Jan-17')
figure.show()


fifties = stats.query("Runs >= 50")
figure = px.bar(fifties, x=fifties["Inns"], y = fifties["Runs"], 
                color = fifties["Runs"],
                title="Fifties By Virat Kohli in First Innings Vs. Second Innings")
figure.show()