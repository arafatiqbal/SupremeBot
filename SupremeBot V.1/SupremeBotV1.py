#Arafat Iqbal
#September 15, 2020
#For Educatinal Purposes Only

from selenium import webdriver
from Store_Your_Info import fill 
from selenium.webdriver.support.ui import Select
import time


def checkout():

	#Make Window Full Screen
	#driver.maximize_window()

	#Checkout item from the URL
	driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
	time.sleep(4)
	driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

	#Fill in Information
	driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(fill['name'])
	driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(fill['email'])
	driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(fill['tel'])
	driver.find_element_by_xpath('//*[@id="bo"]').send_keys(fill['address'])
	driver.find_element_by_xpath('//*[@id="oba3"] ').send_keys(fill['apt'])
	driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(fill['zip'])
	driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(fill['city'])
	#State Is Autofilled

	#Card Info 
	driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(fill['card_num'])
	driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(fill['cvv'])

	#Month and Year
	Month = Select(driver.find_element_by_xpath('//*[@id="credit_card_month"]'))
	time.sleep(0.5)
	Month.select_by_value(fill["card_month"])

	Year = Select(driver.find_element_by_xpath('//*[@id="credit_card_year"]'))
	time.sleep(0.5)
	Year.select_by_value(fill["card_year"])

	#Terms And Conditions
	driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()

	#Process Payment
	driver.find_element_by_xpath('//*[@id="pay"]/input').click()


if __name__ == '__main__':

	PATH = "C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(PATH)

	driver.get(fill['url'])
	checkout()

