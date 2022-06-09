import plotly.figure_factory as ff
import statistics
import random
import csv
import pandas as pd

df = pd.read_csv("newdata110.csv")
data = df["average"].tolist()

pop_mean = statistics.mean(data)
fig = ff.create_distplot([data],["average"],show_hist = False)
fig.show()

mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)
std = statistics.stdev(data)
print(mean,std)

dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean1 = statistics.mean(dataset)
std1 = statistics.stdev(dataset)
print(mean,std1)
