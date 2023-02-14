import pandas as pd
import matplotlib.pyplot as plt
import nltk
#from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS

# load data and drop NA's
df = pd.read_csv("../data/tenet_reviews.csv")
df.dropna()

# assign reviews with rating ge 7 as positive, else negative
df = df[(df['rating'] == 10) | (df['rating'] == 1)]
df['sentiment'] = df['rating'].apply(lambda r: 1 if r == 10 else -1)
positive = df[df['sentiment'] == 1]
negative = df[df['sentiment'] == -1]

# positive word cloud
stopwords = set(STOPWORDS)
stopwords.update(["br", "href", "movie", "tenet", "film", "Nolan", "Christopher", "time",
                  "one", "movies", "watch", "make", "understand"])
pos = " ".join(review for review in positive.review)
wordcloud2 = WordCloud(stopwords=stopwords).generate(pos)
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis("off")
plt.savefig('../images/wordcloud_pos.png')
plt.show()

# negative word cloud
neg = " ".join(review for review in negative.review)
wordcloud3 = WordCloud(stopwords=stopwords).generate(neg)
plt.imshow(wordcloud3, interpolation='bilinear')
plt.axis("off")
plt.savefig('../images/wordcloud_neg.png')
plt.show()
