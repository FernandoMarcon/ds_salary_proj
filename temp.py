import time
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--remote-debugging-port=9222")  # this

driver = webdriver.Chrome(options=chromeOptions)

driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()