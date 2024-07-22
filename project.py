from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "flat-for-rent-in-shastri-nagar"
file = 0
for i in range(1, 20):
 driver.get(f"https://www.olx.in/delhi_g4058659/q-{query}?isSearchCall=true")

 elems = driver.find_elements(By.CLASS_NAME, "_1DNjI")
 print(f"{len(elems)} items found")
 for elem in elems:
   d = elem.get_attribute("outerHTML")
   with open(f"data/{query}_{file}.html", "w" , encoding="utf-8") as f:
     f.write(d)
     file +=1
  #print(elem.text)


 time.sleep(1)
driver.close()