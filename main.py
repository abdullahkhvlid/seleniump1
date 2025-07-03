from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

options = Options()
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)



query = "laptop"
driver = webdriver.Chrome(options=options)
driver.get(f"https://www.amazon.com/s?k={query}")

# wait until real product card loads
WebDriverWait(driver, 15).until(
EC.presence_of_element_located((By.CLASS_NAME, "puis-card-container"))
)

cards = driver.find_elements(By.CLASS_NAME, "puis-card-container")
# print(cards.text)  
for card in cards:
    print(card.text)
    # print(card.get_attribute("outerHTML"))
time.sleep(5)
driver.close()
