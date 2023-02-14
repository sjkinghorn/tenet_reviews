import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/tenet_reviews.csv")

print(df["rating"].isna().sum())
df.dropna()

ratings = df["rating"].value_counts().sort_index(ascending=False) / df.shape[0]
print(ratings)

positive = df[df["rating"] >= 7].shape[0] / df.shape[0]
negative = 1 - positive
print((positive, negative))

sns.displot(df, x="rating", discrete=True)
plt.show()
