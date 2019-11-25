import autoit
import os
import os, random
import shutil
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_argument("--window-size=200,700")
mobile_emulation = { "deviceName": "Nexus 5" }
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--disable-notifications")

import time
from selenium.webdriver.common.by import By

#FACEBOOK'A GÝRÝÞ YAP
#LOGIN FACEBOOK
driver = webdriver.Chrome(executable_path='C:/Users/ELF/Desktop/ELF/Python/chrome/chromedriver.exe',chrome_options=chrome_options)
driver.get("https://m.facebook.com/")
time.sleep(2)
username = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")
username.send_keys("XXXXX")
password.send_keys("XXXXX")
time.sleep(1)
login_box = driver.find_element_by_name('login') 
login_box.click() 
time.sleep(3)
#FACEBOOK'A GÝRÝÞ YAPILDI


#ÝLK FACEBOOK SAYFASI
#FIRST FACEBOOK PAGE
klasor="XXXXXXX"
driver.get("https://www.facebook.com/XXXXX/")
time.sleep(10)
#DOSYA VARMI KONTROL ET. YOKSA HEPSÝNÝ TAÞI
path, dirs, files = next(os.walk("C:\\Users\\ELF\Desktop\\qqq\\z-facebooklar\\"+klasor))
file_count = len(files)
if file_count==0:
    print(klasor+', dosya bittiði için taþýma iþlemi yapýldý.')
    source = 'C:\\Users\\ELF\\Desktop\\qqq\\z-facebooklar\\'+klasor+'\\eklendi\\'
    dest1 = 'C:\\Users\\ELF\Desktop\\qqq\\z-facebooklar\\'+klasor+'\\'
    files = os.listdir(source)
    for f in files:
        shutil.move(source+f, dest1)
#KONTROL EDÝLDÝ
ActionChains(driver).move_to_element( driver.find_element_by_xpath('//*[@id="action_bar"]/div[2]/a')).click().perform()
handle = "[CLASS:#32770; TITLE:Open]"
autoit.win_wait(handle, 60)
dl = os.path.join('C:\\Users\\ELF\Desktop\\qqq\\z-facebooklar\\'+klasor)
go = os.path.join('C:\\Users\\ELF\\Desktop\\qqq\\z-facebooklar\\'+klasor+'\\eklendi')
rastgele_dosya=random.choice([x for x in os.listdir("C:\\Users\\ELF\\Desktop\\qqq\\z-facebooklar\\"+klasor) if os.path.isfile(os.path.join("C:\\Users\\ELF\\Desktop\\qqq\\z-facebooklar\\"+klasor, x))])
uzantisiz_dosya_ismi= rastgele_dosya[:-4]
tam_dosya_ismi = 'C:\\Users\\ELF\Desktop\\qqq\\z-facebooklar\\'+klasor+'\\'+rastgele_dosya
autoit.control_set_text(handle, "Edit1", tam_dosya_ismi)
autoit.control_click(handle, "Button1") #RESÝM SEÇ
time.sleep(1)
result = re.search('eyler yaz..." id="(.+?)"', driver.page_source)
kaynaktaki_istenilen_yazi = (result.group(1))
yazi =kaynaktaki_istenilen_yazi
basi='//*[@id="'
sonu='"]'
bolge = basi + yazi + sonu
driver.find_element_by_xpath(bolge).send_keys(uzantisiz_dosya_ismi) #TEXT BÖLGESÝNE YAZ
time.sleep(12)
#GÖNDER
if driver.find_elements_by_xpath('//*[@id="composer-main-view-id"]/div[1]/div/div[3]/div/button[1]'):
    print("1-"+klasor+ " Paylaþýldý")
    driver.find_element_by_xpath('//*[@id="composer-main-view-id"]/div[1]/div/div[3]/div/button[1]').click()
    time.sleep(5)
    shutil.move(os.path.join(dl, rastgele_dosya), go) #DOSYANIN YERÝNÝ DEÐÝÞ
else:
    time.sleep(2)
    print("1-XXXXXXXXX-PROBLEMLÝ-"+klasor)
time.sleep(3)

driver.close()