
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pprint import pprint

driver=webdriver.Chrome()
url=("https://www.tunisianet.com.tn/pc-portable-tunisie/63884-pc-portable-asus-vivobook-pro-15-ryzen-7-4800h-8-go.html")
driver.get(url)
product={}
title_element=driver.find_element(By.CLASS_NAME, "h1")
title=title_element.text
product["title"]=title

refference_element=driver.find_element(By.CLASS_NAME,"product-reference")
reference=refference_element.text
product["reference"]=reference


description_element=driver.find_element(By.ID,"product-description-short-63884")
description=description_element.text
product["description"]=description


prix_element=driver.find_element(By.CLASS_NAME,"current-price")
prix=prix_element.text
product["prix"]=prix

available_element=driver.find_element(By.ID,"stock_availability")
available=available_element.text
product["available"]=available

all_images=driver.find_elements(By.TAG_NAME,"img")
image=all_images[1].get_attribute("src")
product['image']=image




pprint(product)


time.sleep(1)
driver.close()