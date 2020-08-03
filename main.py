# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys

class InstaBot:
        def __init__(self, username, pw):
            self.driver = webdriver.Chrome()
            self.username = username
            self.driver.get("https://instagram.com")

            self._human_sleep(2)
            
            #Log in
            self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(pw)
            self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
                .click()
            self._human_sleep(4)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
            self._human_sleep(4)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
                
        def get_unfollowers(self):
            self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
                .click()
            self._human_sleep(4)
            self.driver.find_element_by_xpath("//a[contains(@href, 'following')]")\
                .click()
            following = self._get_names()
            print("**** Created list of following ****", flush=True)
            self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]")\
                .click()
            followers = self._get_names()
            print("**** Created list of following ****", flush=True)
            bastards = [user for user in following if user not in followers]
            return bastards
            
        def unfollow_bastards(self, n):
            mofos = self.get_unfollowers()
            print("**** Created list of bastards who didn´t follow you back ****", flush=True)
            self._human_sleep(4)
            self.driver.find_element_by_xpath("//a[contains(@href, 'following')]")\
                .click()
            self._human_sleep(2)
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
            self._load_all_contacts(scroll_box)
            m = n
            while n > 0:
                self._take_naps(n)
                self._human_sleep(2)
                
                name_element = self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(mofos[m-n]))
                antecesor = self._find_ancestor(5, name_element) 
                button = antecesor.find_element_by_xpath(".//button[contains(text(), 'Following')]")


                
                self._human_sleep(5)
                button.click()
                print("**** Stopped following " + mofos[m-n] + " ****")
                self._human_sleep(2)

                self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]")\
                    .click()
                
                self._human_sleep_slow(3)

                n-=1
            
        def talk_to_fans_of(self, account_name, n_of_fans):
                search_bar = self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]")
                search_bar.send_keys(account_name)
                self._human_sleep(3)
                search_bar.send_keys(Keys.RETURN)
                search_bar.send_keys(Keys.RETURN)
                self._human_sleep(4)
                self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]")\
                    .click()
                self._human_sleep(2)
                print("**** Accessing the followers of " + account_name + " ****")
                    
                #Start following people
                followed_list = []
                scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
                for x in range(n_of_fans):
                    button_to_follow = scroll_box.find_element_by_xpath(".//button[text()='Follow']")
                    if button_to_follow == None:
                        self.driver.execute_script("""
                                                   arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                                   return arguments[0].scrollHeight;
                                               """, scroll_box)
                        self._human_sleep(3)
                        continue
                    
                    button_to_follow.click()
                    self._human_sleep(5)
                    antecesor = self._find_ancestor(5, button_to_follow) 
                    button_followed = antecesor.find_element_by_xpath(".//button[contains(text(), 'Following')]")
                    if button_followed != None:
                        name_of_followed = antecesor.find_element_by_xpath(".//a[@href]")
                        name_of_followed.click()
                        followed_list.append(name_of_followed.text)
                        
                        self._human_sleep(1) 
                print(followed_list)
                
        def _get_names(self):
            self._human_sleep(1)
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
            self._load_all_contacts(scroll_box)
            links = scroll_box.find_elements_by_tag_name('a')
            names = [name.text for name in links if name.text != '']
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
                .click()
            return names
        
        def _load_all_contacts(self, scroll_box):
            self._human_sleep(1)
            l_size = 0
            c_size = 1
            while l_size != c_size:
                l_size = c_size
                self._human_sleep_fast(2)
                c_size = self.driver.execute_script("""
                                                    arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                                    return arguments[0].scrollHeight;
                                                    """, scroll_box)
        def _find_ancestor(self, n, element):
            if n == 0:
                return element
            else:
                return self._find_ancestor(n-1, element.find_element_by_xpath('..'))
            
        def _human_sleep(self, n):
            sleep(n + randint(0,3))
        
        def _human_sleep_slow(self, n):
            sleep(n + randint(0,10))
        def _human_sleep_fast(self, n):
            sleep(n + randint(0,1))
        def _take_naps(self, n):
            if n == 4:
                print("**** Napping 5 min ****", flush=True)
                sleep(63*4)
            if n == 10:
                print("**** napping 11 min ****", flush=True)
                sleep(60*12)
            if n == 17:
                print("**** napping 14 min ****", flush=True)
                sleep(52*12)
            if n == 25:
                print("**** napping 3 min ****", flush=True)
                sleep(55*3)
            if n == 30:
                print("**** napping 4 min ****", flush=True)
                sleep(64*5)
            if n == 33:
                print("**** napping 23 min ****", flush=True)
                sleep(60*24)
            if n == 37:
                print("**** napping 6 min ****", flush=True)
                sleep(59*4)
            if n == 40:
                print("**** napping 5 min ****", flush=True)
                sleep(49*6)
            if n == 45:
                print("**** napping 9 min ****", flush=True)
                sleep(57*7)
            if n == 48:
                print("**** Napping 5 min ****", flush=True)
                sleep(56*6)
                            
a_bot = InstaBot('account', 'pass')
a_bot.unfollow_bastards(50)
#a_bot.talk_to_fans_of("artist_name", 1)