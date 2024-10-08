# Nhập các thư viện cần thiết
import pandas as pd
from selenium import webdriver
from time import sleep
import random
import csv
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl.workbook import Workbook

driver = webdriver.Edge()

driver.get("http://facebook.com")
sleep(random.randint(5, 10))

tên_đăng_nhập = driver.find_element(By.ID, "email")
tên_đăng_nhập.send_keys("duuu2001@gmail.com")
sleep(1)

password = driver.find_element(By.ID, "pass")
password.send_keys("Chicananc0m")
password.send_keys(Keys.ENTER)
sleep(1)
df = pd.DataFrame()
links = ['https://www.facebook.com/share/p/9AkEdWud4PAXdeEq/?mibextid=oFDknk','https://www.facebook.com/share/p/sEb5JAZbFrJKYH5G/?mibextid=oFDknk']
for link in links:
    driver.get(link)
    sleep(5)
    clickable = driver.find_element(By.XPATH, '//*')
    ActionChains(driver) \
        .click(clickable) \
        .perform()

    # i = 0
    # while i<10:
    #      scroll = driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    #      sleep(2)

    show_all_comments = driver.find_element(By.XPATH,
                                            '//div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[2]/div/div/span')
    show_all_comments.click()
    sleep(2)
    # show_all = driver.find_element(By.XPATH,
    #                                '//div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]/div/div[1]/span')
    # show_all.click()
    show_all = driver.find_element(By.XPATH,
                                   '//div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]/div/div[1]/span')
    show_all.click()
    i = 0
    while i < 50:
        scroll = driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        i += 1
        sleep(1)

    comment_list = driver.find_elements(By.XPATH, '//div[@role="article"]')
    sleep(random.randint(5, 10))
    times = driver.find_elements(By.XPATH, '//span[@class = "html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"]')
    sleep(5)

    for comment in comment_list:
        try:
            content = comment.find_element(By.XPATH, './/div[@class="x1lliihq xjkvuk6 x1iorvi4"]')
        except:
            continue
        a = content.text
        print(a)
        df = pd.concat([df, pd.DataFrame([a])])
    df = df.reset_index(drop=True)
    df.to_csv('fbcomment.csv', index=False)
