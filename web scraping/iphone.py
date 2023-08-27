from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pprint import pprint


driver=webdriver.Chrome()
url=("https://www.tunisianet.com.tn/smartphone-tunisie/63558-smartphone-apple-iphone-14-pro-max-256-go-noir.html")
driver.get(url)
product={}


title_element=driver.find_element(By.CLASS_NAME, "h1")
title=title_element.text
product["title"]=title


refference_element=driver.find_element(By.ID,"product-description-short-63558")
refference=refference_element.text
product["refference"]=refference



prix_element=driver.find_element(By.CLASS_NAME,"current-price")
prix=prix_element.text
product["prix"]=prix


availability_element=driver.find_element(By.ID,"stock_availability")
available=availability_element.text
product["availibilty"]=available





pprint(product)




