from selenium import webdriver
import time


IMDB_PAGE = "https://www.imdb.com/title/tt6723592/reviews/?ref_=tt_ov_rt"
driver = webdriver.Chrome('C:/Users/sjkin/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(IMDB_PAGE)

while True:
    try:
        loadMoreButton = driver.find_element_by_css_selector("button.ipl-load-more__button")
        time.sleep(2)
        loadMoreButton.click()
        time.sleep(5)
    except Exception as e:
        print(e)
        break
print("Complete")
time.sleep(10)
with open("../data/imdb_tenet_reviews.html", "w", encoding='utf-8') as f:
    f.write(driver.page_source)
driver.quit()
