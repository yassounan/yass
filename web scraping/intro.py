#from selenium import webdriver
#import time

#driver=webdriver.Chrome()
#driver.get("https://www.youtube.com/watch?v=-UI5GpNbD4M")
#time.sleep(60)





from selenium import webdriver
import time
from pprint import pprint



from get_product import get_product

options=webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver=webdriver.Chrome(options=options)
url=("https://www.tunisianet.com.tn/pc-portable-tunisie/63884-pc-portable-asus-vivobook-pro-15-ryzen-7-4800h-8-go.html")
product=get_product(driver,url)
pprint(product)

time.sleep(1)
driver.close