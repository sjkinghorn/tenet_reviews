from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# page = requests.get("https://www.imdb.com/title/tt6723592/reviews/?ref_=tt_ov_rt")
# soup = BeautifulSoup(page.content, 'html.parser')

with open("../data/imdb_tenet_reviews.html", encoding="utf8") as page:
    soup = BeautifulSoup(page, 'html.parser')

ratings = []
reviews = []
users = soup.select("div.imdb-user-review")
for i in range(len(users)):
    rating = users[i].select("span.rating-other-user-rating span:first-of-type")
    if rating:
        ratings.append(rating[0].get_text())
    else:
        ratings.append(np.nan)
    review = users[i].select("div.text.show-more__control")
    if review:
        r = " ".join(review[0].get_text().splitlines())  # remove line breaks
        reviews.append(r)
    else:
        reviews.append(np.nan)

movie_reviews = pd.DataFrame({
    "rating": ratings,
    "review": reviews
})

print(movie_reviews)
movie_reviews.to_csv("../data/tenet_reviews.csv", index=False)

# # ratings
# selector = soup.select("span.rating-other-user-rating span:first-of-type")
# ratings = [s.get_text() for s in selector]

# # reviews
# selector = soup.select("div.text.show-more__control")
# reviews = [s.get_text() for s in selector]

# print(len(ratings), len(reviews))
