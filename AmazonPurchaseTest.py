import base64

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

driver = webdriver.Chrome("/Users/pv303y/PycharmProjects/pythonProject/drivers/chromedriver")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://amazon.in")
window_before = driver.window_handles[0]
print ("Parent Window : " + window_before)
driver.find_element_by_xpath("//a[contains(text(),'Mobiles')]").click()
driver.find_element_by_xpath("//span[contains(text(),'Apple')]").click()
driver.execute_script("window.scrollBy(0,2000)", "")
driver.find_element_by_xpath("//span[contains(text(),'Apple iPhone 13 Pro Max (256GB) - Sierra Blue')]").click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
print ("Child Window : " + window_after)
driver.execute_script("window.scrollBy(0,350)", "")
driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
driver.find_element_by_xpath("//a[@id='attach-close_sideSheet-link']").click()
driver.execute_script("window.scrollBy(0,-600);")
# driver.find_element_by_xpath("//header/div[@id='navbar']/div[@id='nav-progressive-subnav']/div[@id='nav-subnav']/a[2]/span[1]").click()
driver.find_element_by_xpath("//span[contains(text(),'Mobiles & Accessories')]").click()
#To Comment Use Control+/
# driver.find_element_by_xpath("//span[contains(text(),'Mobile Accessories')]").click()
# driver.execute_script("window.scrollBy(0,700)", "")
# driver.find_element_by_xpath("//span[contains(text(),'Headsets')]").click()
#driver.find_element_by_xpath("//body/div[@id='a-page']/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/a[1]/img[1]").click()
# driver.find_element_by_xpath("//span[contains(text(),'Apple AirPods Pro')]").click()
# window_after2 = driver.window_handles[2]
# driver.switch_to.window(window_after2)
# print ("Second Child Window : " + window_after2)
# time.sleep(2)
# driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
# driver.find_element_by_xpath("//span[@id='nav-cart-count']").click()
# driver.find_element_by_name("proceedToRetailCheckout").click()
#
# #Enter your Credentials
# driver.find_element_by_id("ap_email").send_keys("richa1085@gmail.com")
# driver.find_element_by_id("continue").click()
# password = "mayank123".encode("utf -8")
# print (password)
# encoded = base64.b64encode(password)
# print("Encoded Password: "+encoded)
# driver.find_element_by_id("ap_password").send_keys(encoded)
# driver.find_element_by_id("signInSubmit").click()
time.sleep(4)
driver.close()
driver.quit()
# print("Test Completed")


