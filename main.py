import csv
from selenium import webdriver
import pandas
from pandas import DataFrame
import requests

test_url = "https://downtowndallas.com/experience/stay/"

chrome_driver_path = "E:\softwares/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(test_url)

driver.find_element_by_xpath("/html/body").click()

driver.back()

driver.find_element_by_xpath("/html/body/main/div/section[2]/div[1]/div[3]/a").click()

place_name = driver.find_element_by_css_selector(".place-header h1").text
print(place_name)

address = driver.find_element_by_xpath("/html/body/main/article/div/div[1]/div[1]/a").text
print(address)

phone = driver.find_element_by_xpath("/html/body/main/article/div/div[1]/div[2]/div/a").text
print(phone)

area = driver.find_element_by_xpath("/html/body/main/article/div/div[1]/div[3]/a").text
print(area)

image = driver.find_element_by_css_selector(".place-info-image img")
image_src = image.get_attribute("src")
print(image_src)

driver.get(image_src)
driver.save_screenshot("AC-Marriott.png")

hotel_dict = [
    {
        'Name': place_name,
        'Address': address,
        'Phone': phone,
        'Area': area,
        'Image-url': image_src,
    }
]
print(hotel_dict)

data = pandas.DataFrame(hotel_dict)
data.to_csv('record.csv')
