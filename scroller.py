from selenium import webdriver
import time

if len(sys.argv) != 2:
    print("Usage: scroller.py <url of channel videos page>")
    sys.exit(1)

url = sys.argv[1]
scroll_pause_time = 1

driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight;")
while True:
    driver.execute_script("window.scroll(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight;")
    if new_height == last_height:
        break
    last_height = new_height

driver.close()
