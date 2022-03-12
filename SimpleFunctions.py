from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome("/Users/pv303y/PycharmProjects/pythonProject/drivers/chromedriver")
# driver = webdriver.Firefox()
# driver = webdriver.ie()

# To open Google.com and search for Text
# driver.set_page_load_timeout(10)
# driver.get("http://google.com")
# driver.find_element_by_id("L2AGLb").click()
# driver.find_element_by_name("q").send_keys("Automation step by step")
# driver.find_element_by_name("q").send_keys(Keys.ENTER)
# time.sleep(4)
# driver.close()

# List
lucky_numbers = [4, 6, 11, 18, 19]
friends = ["Kevin", "Maria", "Richard", "Mike", "Hari"]
friends.sort()
print (friends)

# tuples
coordinates = (4, 5)
print (coordinates[0])


# functions
def say_hello(name, age):
    print ("Hello " + name + ", you are " + age)


# call the fuction
say_hello("Mike", "45")


# return
def cube(num):
    return num * num * num


print (cube(4))

# use of IF ELSE
is_male = True
is_tall = False

if is_male and is_tall:
    print (" You are male or tall")
elif is_male and not (is_tall):
    print ("you are a short one")
else:
    print ("you are neither")

# build a calculator
import math

num1 = float(input("Enter the 1st number: "))
op = input("Enter operator: ")
num2 = float(input("Enter the 2nd number: "))

if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "*":
    print (num1 * num2)
elif op == "/":
    print (num1 / num2)
else:
    print ("Invalid Operator")

# dictionary
monthconversions = {
    "Jan": "January",
    4: "April",
    12: "December",
    "Feb": "February",
}
print (monthconversions.get(4))

# while loop
i = 2
while i <= 4:
    print (i)
    i = i + 1

print("Completed the loop")
