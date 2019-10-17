from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pyvirtualdisplay import Display

from time import sleep
import parsing
import calendar
import sys
import os

import getpass

def main():

    display = Display(visible=0, size=(800, 800))    
    display.start()
    print('Virtual display done.')

    hw_name = input('作業下載路徑: ')
    if not os.path.exists(hw_name):
        os.makedirs(hw_name)

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    prefs = {'profile.default_content_settings.popups': 0,
             'download.default_directory': os.path.join(os.getcwd(), hw_name), #Must end with slash e.g. 'hw1/'
             #'download.prompt_for_download': False,
             'directory_upgrade': True}

    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(chrome_options=options)

    browser.get("https://ceiba.ntu.edu.tw/index.php")
    browser.find_element_by_xpath('//input[@value="1"]').click()

    name = browser.find_element_by_name("loginid")
    pw = browser.find_element_by_name("password")

    user_name = input('請輸入ceiba帳號: ')
    password = getpass.getpass('請輸入ceiba密碼: ')

    name.send_keys(user_name)
    pw.send_keys(password)

    browser.find_element_by_xpath("//input[@class='btn'][@type='submit'][@value='登入']").submit()
    browser.find_element_by_name("b1").click()
    browser.find_element_by_xpath("//input[@onclick=\"singleadm('hw')\"]").click()
    browser.find_element_by_link_text("批改作業").click()

    hwID = input('請輸入作業編號: ')
    browser.find_element_by_xpath("//input[@onclick=\"singlehw('%s')\"]" %hwID).click()

    browser.find_element_by_link_text("此作業所有列表").click()
    all_file_links = browser.find_elements_by_link_text("繳交檔案")
    
    for hw in all_file_links:
        hw.click()
        sleep(1)

    browser.quit()


if __name__ == "__main__":
    main()
