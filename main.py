# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from random import randint
from selenium.common.exceptions import NoSuchElementException


class InstaBot:
        def __init__(self, username, pw):
            self.driver = webdriver.Chrome()
            self.username = username
            self.driver.get("https://instagram.com")

            self._human_sleep(2)
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
            if n == 5:
                print("**** Napping 5 min ****", flush=True)
                sleep(63*5)
            if n == 12:
                print("**** napping 11 min ****", flush=True)
                sleep(60*11)
            if n == 20:
                print("**** napping 14 min ****", flush=True)
                sleep(52*14)
            if n == 24:
                print("**** napping 3 min ****", flush=True)
                sleep(55*3)
            if n == 29:
                print("**** napping 4 min ****", flush=True)
                sleep(64*4)
            if n == 31:
                print("**** napping 23 min ****", flush=True)
                sleep(60*23)
            if n == 37:
                print("**** napping 6 min ****", flush=True)
                sleep(59*6)
            if n == 42:
                print("**** napping 5 min ****", flush=True)
                sleep(49*5)
            if n == 46:
                print("**** napping 9 min ****", flush=True)
                sleep(57*9)
            if n == 49:
                print("**** Napping 5 min ****", flush=True)
                sleep(56*5)
            
                     
a_bot = InstaBot('account', 'pass')
a_bot.unfollow_bastards(50)