from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver

driver = webdriver.Chrome()
for x in range (1,2):
	driver.get("https://armtek.ru/assortment/category/rulevye-reyki-9255?PRICE%5BMIN_VALUE%5D=3000&PRICE%5BMAX_VALUE%5D=100000&viewType=list"+"&page="+str(x))
	time.sleep(5)
	prvs = ''
	elements_number = driver.find_elements(By.XPATH , "//div[@class='content']/div[1]/div[1]/div[3]/a")
	elements_brand = driver.find_elements(By.XPATH , "//div[@class='content']/div[1]/div[1]/div[3]/span[1]")
	elements_price = driver.find_elements(By.XPATH , "//div[@class='content']//div[2]/project-ui-article-card-suggestions[1]//div[@class='card__price-container']/div[1]")
	elements_name = driver.find_elements(By.XPATH , "//div[@class='content']//div[@class='item-info-row']")
	brand_count = 0
	for i in elements_number:

		r = str(i.text)
		try:
				b = str(elements_brand[brand_count].text)
				p = str(elements_price[brand_count].text)
				n = str(elements_name[brand_count].text)
		except Exception as e:
				pass
		else:
				pass	
		with open("RULEVIE REIKI.txt", "a", encoding="utf-8") as f:
			
				
			f.write(r + ";"+b+";"+p+";"+n+";"+"\n")

		print(r + ";"+b+";"+p+";"+n+";"+"\n")
		brand_count+=1
		print(len(elements_number))
		print(len(elements_brand))
		print(len(elements_price))
		print(len(elements_name))
		prvs = r

driver.quit()



