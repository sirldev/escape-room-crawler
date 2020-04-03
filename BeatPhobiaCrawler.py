# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# ChromeDriver로 접속
driver = webdriver.Chrome('./chromedriver')

# 웹페이지 호출
driver.get("https://www.xphobia.net/reservation/reservation_check.php")


# 카테고리 정보
def get_category():
  categories = driver.find_element_by_class_name('cate_select').find_elements_by_tag_name('li')
  for category in categories:
    print(category.text)
  return categories

# 지점 정보
def get_shop(category):
  driver.find_element_by_xpath("//*[contains(text(), '{category}')]".format(category=category)).click()
  time.sleep(1)
  shops = driver.find_element_by_class_name('shop_select').find_elements_by_tag_name('li')
  for shop in shops:
    print(shop.text)
  return shops

# 테마 정보
def get_theme(category, shop):
  get_shop(category)
  driver.find_element_by_xpath("//*[contains(text(), '{shop}')]".format(shop=shop)).click()
  time.sleep(1)
  themes = driver.find_element_by_class_name('quest_select').find_elements_by_tag_name('li')
  for theme in themes:
    print(theme.text)
  return themes

# 시간 정보
def get_time(category, shop, theme):
  get_theme(category, shop)
  driver.find_element_by_xpath("//*[contains(text(), '{theme}')]".format(theme=theme)).click()
  time.sleep(4)
  times = driver.find_element_by_class_name('time_select').find_elements_by_tag_name('li')
  for item in times:
    if "time_lock" not in item.get_attribute('class'):
      print(item.text)
  return times

get_time('포비아 던전','서면 던전','꿈의 공장')

driver.close()