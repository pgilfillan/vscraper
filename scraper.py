import pickle
from selenium import webdriver
import time
import re
import sys

if len(sys.argv) != 2:
    print("Usage: scraper.py <url of channel videos page>")
    sys.exit(1)

url = sys.argv[1]
scroll_pause_time = 1

driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

videos = []
last_height = driver.execute_script("return document.body.scrollHeight;")
while True:
    driver.execute_script("window.scroll(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight;")
    if new_height == last_height:
        break
    last_height = new_height

elems = driver.find_elements_by_css_selector(".article_content.-video")
for elem in elems:
    date = elem.find_element_by_class_name("time").text
    date = re.sub(r'(.*)\. (.*)\. (.*)\..*', "\g<1>/\g<2>/\g<3>", date)
    url = elem.find_element_by_class_name("article_link").get_property("href")
    title = elem.find_element_by_class_name("title").text
    videos.append([title, date, url])
    
with open('videos.data', 'wb') as f:
    pickle.dump(videos, f)

driver.quit()
