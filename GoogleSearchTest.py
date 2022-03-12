import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import unit test module
import unittest


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='/Users/pv303y/PycharmProjects/pythonProject/drivers/chromedriver')
        # set the implicit wait for 10 sec
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_AutomationStepByStep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_id("L2AGLb").click()
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        time.sleep(2)
        print ("Test1 Completed")

    def test_search_Name(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Richa Bagrodia")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        time.sleep(1)
        print ("Test2 Completed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print ("Test Completed")


if __name__ == '__main__':
    unittest.main()


#Run Unittest through the Command Prompt
# cd /Users/pv303y/PycharmProjects/pythonProject/SampleProject1
# python3.10 GooglesearchTest.py
#to get the list of files type ls
