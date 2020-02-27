from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import random
Path="C:\ChromeDriver2\chromedriver.exe"
Drive = webdriver.Chrome(Path)
def InstagramLogin():
    password=password
    username=username
    Drive.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    time.sleep(each_delay_to_load_or_refresh)
    SearchBox = Drive.find_element_by_name("username")
    SearchBox.send_keys(username)
    SearchBox = Drive.find_element_by_name("password")
    SearchBox.send_keys(password)
    SearchBox.send_keys(Keys.ENTER)
    time.sleep(each_delay_to_load_or_refresh)
    Class=Drive.find_element_by_class_name("HoLwm").click()
def OpenSookhtejet():
    SearchBoxInstagram = Drive.find_element_by_class_name("x3qfX")
    NameSAccountToFollow_its_Followers=["sookhtejet.ir","success_fullness","exitomag","selfmade_ir","shaahrah","capsule_zehneservatsaz","morabiye_zehn","sayeh__roshan","movafaghiat__official",'tavana_sho',"parsi_millionaire","mentorplus.ca","movafaghiyat_club","shahre_movafaghiat","havin.anghizeshi"]
    NameAccountToFollow_its_Followers=random.choice(NameSAccountToFollow_its_Followers)
    SearchBoxInstagram.send_keys(NameAccountToFollow_its_Followers)
    time.sleep(each_delay_to_load_or_refresh)
    SearchBoxInstagram.send_keys(Keys.RETURN)
    SearchBoxInstagram.send_keys(Keys.ENTER)
def OpenFollowers():
    time.sleep(each_delay_to_load_or_refresh)
    Followers = Drive.find_elements_by_class_name("g47SY")
    print (len(Followers))
    print (str(Followers))
    Followers[1].click()
def FollowersAnalyse():
    def ScrollDown():
        elm=Drive.find_element_by_tag_name('html')
        elm.send_keys(Keys.END)
    time.sleep(each_delay_to_load_or_refresh)
    Followers=[1]
    if True:
        t=0
        PanelFollowers=Drive.find_element_by_class_name("HYpXt")
        while len(Followers)<number_of_accounts_to_be_found_in_followers_tab:
            time.sleep(random.randint(minimum_delay_scroll_down,maximum_delay_scroll_down))
            PanelFollowers.click()
            ScrollDown()
            Followers = (Drive.find_elements_by_class_name("y3zKF"))
        for Each in Followers:
            t+=1
            if Each.text=="Follow":
                time.sleep(random.randint(minimum_delay_to_follow,maximum_delay_to_follow))
                Each.click()
        time.sleep(each_delay_to_load_or_refresh)

while True:
    InstagramLogin()
    OpenSookhtejet()
    OpenFollowers()
    FollowersAnalyse()
    Drive.close()