#twitter follower
#by saty035
# @heysaty twitter

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #we can add input or hit enter key
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox()

    def login(self):
        bot=self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        username=bot.find_element_by_name("session[username_or_email]")
        password=bot.find_element_by_name("session[password]")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot=self.bot 
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        for i in range(3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)

saty=TwitterBot('username','password')
saty.login()
saty.like_tweet('python')
