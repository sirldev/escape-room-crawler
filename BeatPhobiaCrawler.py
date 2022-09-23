# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ChromeDriver로 접속
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 웹페이지 호출
driver.get("https://www.xphobia.net/reservation/reservation_check.php")


# 카테고리 정보
def get_category():
    categories = driver.find_element(By.CLASS_NAME, 'cate_select').find_elements((By.TAG_NAME, 'li'))
    for category in categories:
        print(category.text)
    return categories


# 지점 정보
def get_shop(category):
    driver.find_element(By.XPATH, "//*[contains(text(), '{category}')]".format(category=category)).click()
    time.sleep(1)
    shops = driver.find_element(By.CLASS_NAME, 'shop_select').find_elements(By.TAG_NAME, 'li')
    for shop in shops:
        print(shop.text)
    return shops


# 테마 정보
def get_theme(category, shop):
    get_shop(category)
    driver.find_element(By.XPATH, "//*[contains(text(), '{shop}')]".format(shop=shop)).click()
    time.sleep(1)
    themes = driver.find_element(By.CLASS_NAME, 'quest_select').find_elements(By.TAG_NAME, 'li')
    for theme in themes:
        print(theme.text)
    return themes


# 시간 정보
def get_time(category, shop, theme):
    get_theme(category, shop)
    driver.find_element(By.XPATH, "//*[contains(text(), '{theme}')]".format(theme=theme)).click()
    time.sleep(4)
    times = driver.find_element(By.CLASS_NAME, 'time_select').find_elements(By.TAG_NAME, 'li')
    for item in times:
        if "time_lock" not in item.get_attribute('class'):
            print(item.text)
    return times


get_time('포비아 던전', '서면 던전', '꿈의 공장')

driver.close()
