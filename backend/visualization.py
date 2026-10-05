import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dataset/twitter_data.csv")

df['sentiment'].value_counts().plot(kind='bar')

plt.title("Sentiment Distribution")

plt.show()