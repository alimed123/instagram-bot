from selenium import webdriver
import selenium.webdriver.common.keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import load_workbook
from selenium.webdriver.support import expected_conditions as EC
import random
driver=webdriver.Firefox()
driver.get("https://www.instagram.com")
username1=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
password1=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
username1.clear()
password1.clear()
username1.send_keys("SCRAPING123s")
password1.send_keys("SCRAPE")
log_in=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
import time
time.sleep(3)
continueh=True
while continueh:
    link=input("enter link")
    try:
        driver.get(link)
        followers_instagram=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span").get_attribute("title").replace(",","")
        following_instagram=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span").text.replace(",","")
    except:
        driver.refresh()
        followers_instagram=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span").get_attribute("title").replace(",","")
        following_instagram=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span").text.replace(",","")
    #checking_followers
    fo=[]
    followerss=[]
    print(followers_instagram)
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//section/ul/li[2]"))).click()
    for _ in range(round( int(followers_instagram) // 10)):
        time.sleep(3)
        driver.find_element_by_xpath("//div[6]/div/div/div/div[2]").send_keys(Keys.END)
        time.sleep(3)
        followers = driver.find_elements_by_xpath('//div/div/span/a')

        # Getting url from href attribute
        for x in followers:
            if x.get_attribute("href"):
                followerss.append(x.get_attribute("href"))
    followerss=set(followerss)
    print(len(followerss))
    likes=0
    for i in followerss:
        try:
            driver.get(i)
            check=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section/main/div/div/article"))).text
        except:
            driver.refresh()
            check=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section/main/div/div/article"))).text
        if "This account is private" not in check:
            if int(WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//section/ul/li[2]"))).text.replace(" followers","").replace(" follower","").replace(",","")) >500:
                try:
                    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class='eLAPa']"))).click()
                    import datetime
                    today= datetime.datetime.today()
                    from datetime import *
                    check=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[2]/div/a/div/time"))).get_attribute("datetime").replace(".000Z","")
                    checky=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[2]/div/a/div/time"))).get_attribute("datetime").replace(".000Z","")
                    checky=datetime.strptime(checky,"%Y-%m-%dT%X")
                    number_of_weeks=abs(today-checky).days
                    if number_of_weeks/7 <7:
                        for insta_liky in range(5):
                            try:
                                p=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".EDfFK > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)"))).text
                            except:
                                insta_liky=insta_liky-1
                                pass
                            try:
                                small_check=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div'))).text
                                if "Liked by" in small_check:
                                    p=0
                                else:
                                    p=p.replace(",","").replace(" likes","").replace(" like","")
                                    if int(p) >5000:
                                        fo.append(i)
                                        break
                            except:
                                insta_liky=insta_liky-1
                            WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class=' l8mY4 feth3']/button"))).click()
                            likes=likes+int(p)
                        print(likes/5)
                        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[@aria-label='Close']"))).click()
                        if int(likes/5) >=70:
                            fo.append(i)
                        likes=0
                except:
                    pass
    driver.get(link)
    followingg=[]
    import time
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//section/ul/li[3]"))).click()
    for _ in range(round( int(following_instagram) // 10)):
        time.sleep(3)
        driver.find_element_by_xpath("//div[6]/div/div/div/div[3]").send_keys(Keys.END)
        time.sleep(3)
        following = driver.find_elements_by_xpath('//div/div/span/a')

        # Getting url from href attribute
        for iww in following:
            if iww.get_attribute("href"):
                followingg.append(iww.get_attribute("href"))
    followingg=set(followingg)
    print(len(followingg))
    likes=0
    for ix in followingg:
        try:
            driver.get(ix)
            check=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section/main/div/div/article"))).text
        except:
            driver.refresh()
            check=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section/main/div/div/article"))).text
        if "This account is private" not in check:
            if int(WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//section/ul/li[2]"))).text.replace(" followers","").replace(" follower","").replace("k","00").replace(".","").replace("m","00000").replace(",","")) >500:
                try:
                    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class='eLAPa']"))).click()
                    import datetime
                    today= datetime.datetime.today()
                    from datetime import *
                    check=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[2]/div/a/div/time"))).get_attribute("datetime").replace(".000Z","")
                    checky=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[2]/div/a/div/time"))).get_attribute("datetime").replace(".000Z","")
                    checky=datetime.strptime(checky,"%Y-%m-%dT%X")
                    number_of_weeks=abs(today-checky).days
                    if number_of_weeks/7 <7:
                        for insta_liky in range(5):
                            try:
                                p=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".EDfFK > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)"))).text
                            except:
                                insta_liky=insta_liky-1
                                pass
                            try:
                                small_check=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div'))).text
                                if "Liked by" in small_check:
                                    insta_liky=insta_liky-1
                                    pass
                                else:
                                    p=p.replace(",","").replace(" likes","").replace(" like","")
                                    if int(p)>5000:
                                        fo.append(ix)
                                        break
                            except:
                                insta_liky=insta_liky-1
                            WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@class=' l8mY4 feth3']/button"))).click()
                            likes=likes+int(p)
                        print(likes/5)
                        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[@aria-label='Close']"))).click()
                        if int(likes/5) >=70:
                            fo.append(ix)
                        likes=0
                except:
                    pass
    fo=list(set(fo))
    data={"Links":fo}
    df=pd.DataFrame(data)
    df.to_excel("output.xlsx",engine="openpyxl")
    continueh=input("do you want to continue?y/N")
    if continueh=="y" or continueh=="Y":
        continueh=True
    elif continueh=="n" or continueh=="N":
        continueh=False
    else:
        continueh=input("worng input please enter y/N")
        if continueh=="y" or continueh=="Y":
            continueh=True
        elif continueh=="n" or continueh=="N":
            continueh=False
