#load webdriver function from selenium
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup, Comment
import pandas as pd
import re
import requests
from optparse import OptionParser
from matplotlib.cbook import dedent
import json
import time

#Setting up Chrome webdriver Options
chrome_options = webdriver.ChromeOptions()

#setting  up local path of chrome binary file
chrome_options.binary_location = r"D:/AnacondaFiles/chromedriver_win32/chromedriver.exe"

#creating Chrome webdriver instance with the set chrome_optionsX
driver = webdriver.Chrome(executable_path=r'D:/AnacondaFiles/chromedriver_win32/chromedriver.exe')

link = "https://play.google.com/store/apps/details?id=com.dai.uangteman&showAllReviews=true"
driver.get(link)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
Ptitle = driver.find_element_by_class_name('AHFaub').text#.replace(' ','')
print(Ptitle)
#driver.find_element_by_xpath('//*[@id="body-content"]/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button[2]/div[2]').click()

#sleep(1)
#driver.find_element_by_xpath('//*[@id="body-content"]/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button[2]/div[2]/div/div').click()
#select_newest.select_by_visible_text('Newest')
#driver.find_element_by_xpath('//*[@id="body-content"]/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button[2]/div[2]/div/div').click()
#sleep(2)
#driver.find_element_by_css_selector('.review-filter.id-review-sort-filter.dropdown-menu-container').click()
#driver.find_element_by_css_selector('.displayed-child').click()
#driver.find_element_by_xpath("//button[@data-dropdown-value='1']").click()
#driver.execute_script("document.querySelectorAll('button.dropdown-child')[0].click()")
reviews_df = []


# headers = {
#         "CONSENT":"YES+IT.it+20160117-18-0",
#     }

# data = {
#         "reviewType": 0,
#         #"pageNum" :page,
#         #"id":id,
#         "reviewSortOrder":4,
#         "xhr": 1,
#         "hl":"it"
#     }

# r = requests.post("https://play.google.com/store/getreviews?authuser=0", headers=headers, data=data)
time.sleep(10);
for i in range(1,50000):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   # time.sleep(1)

for i in range(1,2):
    try:
        for elem in driver.find_elements_by_class_name('d15Mdf'):
            
            print(str(i))
            content = elem.get_attribute('outerHTML')
            soup = BeautifulSoup(content, "html.parser")
            #print(soup.prettify())
            user = soup.find('span',class_='X43Kjb').get_text()
            date = soup.find('span',class_='p2TkOb').get_text()
            #rating = soup.find('span',class_='nt2C1d')['aria-label'][6:7]
            #rating = driver.find_element_by_class_name('pf5lIe').text
            #rating = soup.find('div', {'class':'pf5lIe'}).text[6:7]
            rating = soup.findAll("div", {"class" : "pf5lIe"})
            
            txt_before = soup.find('div',class_='UD7Dzf').get_text().replace('Full Review','')#[len(user)+1:]
            txt = txt_before.replace('\n',' ')
            print(soup.get_text())
            temp = pd.DataFrame({'User':user,'Date':date,'Rating':rating,'Review Text':txt},index=[0])
            print('-'*10)
            reviews_df.append(temp)
    
#print(elem)
    except:
        print('s')
    try:
        driver.find_element_by_css_selector('div.U26fgb.O0WRkf.oG5Srb.C0oVfc.n9lfJ.M9Bg4d.content.CwaK9.span.RveJvd.snByac').click()
    #driver.find_elements_by_class_name('RveJvd').click()
    except:
        continue
#driver.find_element_by_css_selector("div.U26fgb.O0WRkf.oG5Srb.C0oVfc.n9lfJ.M9Bg4d.content.CwaK9.span.RveJvd.snByac").click()
reviews_df = pd.concat(reviews_df,ignore_index=True)

reviews_df.to_csv(Ptitle+'_reviews_list.csv', encoding='utf-8')

#driver.close()
