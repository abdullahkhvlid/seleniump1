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


file = 0
query = "laptop"
driver = webdriver.Chrome(options=options)
for i in range(1, 20):    
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&crid=2XCMULCO5BD73&sprefix=laptop%2Caps%2C313&ref=nb_sb_noss_1")

    # wait until real product card loads
    WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "puis-card-container"))
    )

    cards = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    for card in cards:
        d = card.get_attribute("outerHTML")
        with open(f"data/{query}_{file}_file.html" , "w", encoding="utf-8") as f:
            f.write(d)
            file = file + 1
driver.close()
