import requests
import lxml
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import UnexpectedAlertPresentException


url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61666335058594%2C%22east%22%3A-122.24999464941406%2C%22south%22%3A37.619361681932645%2C%22north%22%3A37.93089304244048%7D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A438568%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2500%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
header = {
    'User-Agent': "jiaojiaokuaidianhaoqilaifighting",
    'Accept-Language': "jiaojiaokuaidianhaoqilaifighting",
}
GOOGLE_FORMS = "https://docs.google.com/forms/d/e/1FAIpQLSfgWmgBrocLDE1B50B-dXBAnACCXSM93i0IuD-6zYu3qIFwBw/viewform?usp=sf_link"

# response = requests.get(url, headers=header)
# print(response.content)
# soup = BeautifulSoup(response.content, "lxml")

with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")

addresses_origin = soup.select("#grid-search-results ul li address")
addresses = [address.getText() for address in addresses_origin]
prices_origin = soup.select("#grid-search-results ul li .PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")
prices = [price.getText().split()[0] for price in prices_origin]
links_origin = soup.select("#grid-search-results ul li .property-card-data a")
links = [link.get('href') for link in links_origin]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')  # 禁用通知
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(prices)):
    sleep(5)
    try:
        driver.get(GOOGLE_FORMS)
        address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(addresses[0])
        price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(prices[0])
        link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input.send_keys(links[0])
        link_input.send_keys(Keys.ENTER)
    except UnexpectedAlertPresentException:
        alert = driver.switch_to.alert
        alert.dismiss()

driver.get("https://docs.google.com/forms/d/1dLW3kqMj1IRLwZzQOf3iurFl-E3NT6EAm4S7XNeJgVk/edit#responses")
links_to_sheets = driver.find_element(By.XPATH, value='//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]')
links_to_sheets.click()









