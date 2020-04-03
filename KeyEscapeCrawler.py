# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# ChromeDriver로 접속
driver = webdriver.Chrome('./chromedriver')

# 웹페이지 호출
driver.get("https://keyescape.co.kr/web/home.php?go=rev.make")

point = input()
theme = input()


# 지점 설정
def set_point(input):
  point = driver.find_element_by_id('zizum_data').find_element_by_partial_link_text(input)
  point.click()


# 날짜 설정
def set_date(input):
  dates = driver.find_element_by_class_name('t_calendar').find_elements_by_tag_name('a')
  for date in dates:
    print(date.text + '일')
    date.send_keys(Keys.ENTER)
    time.sleep(1)
    set_theme(input)
    time.sleep(1)


# 테마 설정
def set_theme(input):
  theme = driver.find_element_by_id('theme_data').find_element_by_link_text(input)
  theme.click()
  time.sleep(2)
  set_time()


# 시간 설정
def set_time():
  time = driver.find_element_by_id('theme_time_data').find_elements_by_class_name('possible')
  print(str(len(time)) + '개 가능')
  for item in time:
    print(item.text)


set_point(point)
time.sleep(1)
set_date(theme)

driver.close()
