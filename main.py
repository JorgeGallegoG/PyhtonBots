# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
import math

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
        _following_path = ".\data"
        _following_file_name = "following"
                
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
                    flag = False
                    while flag == False:
                        self._human_sleep(5)
                        try:
                            button_to_follow = scroll_box.find_element_by_xpath(".//button[text()='Follow']")
                            flag = True
                        except NoSuchElementException:
                            self.driver.execute_script("""
                                                       arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                                       return arguments[0].scrollHeight;
                                                   """, scroll_box)
                            self._human_sleep(3)
                            continue
                    button_to_follow.click()
                    self._human_sleep(5)
                    antecesor = self._find_ancestor(3, button_to_follow)
                    list_name_of_followed_b = antecesor.find_elements_by_tag_name('a')
                    temp_list_names_of_followed_text = [name.text for name in list_name_of_followed_b if name.text != '']
                    name_of_followed = antecesor.find_element_by_xpath(".//a[@href]")
                    try:
                        button_followed = antecesor.find_element_by_xpath(".//button[contains(text(), 'Following')]")
                        name_of_followed.click()
                        self._human_sleep(3)
                        print(temp_list_names_of_followed_text[0])
                        followed_list.extend(temp_list_names_of_followed_text)
                        self.driver.find_element_by_xpath("//button[contains(text(), 'Message')]")\
                        .click()
                        self._send_messages()
                        self._human_sleep_fast(2)
                        self.driver.execute_script("window.history.go(-1)")
                        self._human_sleep(4)
                        self.driver.execute_script("window.history.go(-1)")
                    except NoSuchElementException:
                        pass
                        
                    self._human_sleep(1)
                    temp_list_names_of_followed_text = []
                    print("**** CUCA ****")
                    self._human_sleep(4)
                    scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]")
                with open (self._following_path + self._following_file_name + ".csv",'a') as following_file:
                    writer = csv.writer(following_file, dialect='excel')
                    writer.writerow(followed_list)
                    self._human_sleep(4)
                    self.driver.execute_script("window.history.go(-1)")
                    self._human_sleep(5)
                    self.driver.execute_script("window.history.go(-1)")
                    self._human_sleep(3)
                    self.driver.execute_script("window.history.go(-1)")
               
        def _send_messages(self):
            list_messages = self._generate_messages()
            self._human_sleep(6)
            for msg in list_messages:
                message_bar = self.driver.find_element_by_xpath("//textarea[@placeholder=\"Message...\"]")
                #Using javascript to send emojis (not suported by send kesys method)
                JS_ADD_TEXT_TO_INPUT = """
                                      var elm = arguments[0], txt = arguments[1];
                                      elm.value += txt;
                                      elm.dispatchEvent(new Event('change'));
                                      """
    
                self.driver.execute_script(JS_ADD_TEXT_TO_INPUT, message_bar, msg)
                self._human_sleep(10)
                #message_bar.click()
                message_bar.send_keys(" ")
                self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]")\
                   .click()
                

                self._human_sleep(3)
            
        #Method to generate a list of messages that when put toguether generate a conversation
        def _generate_messages(self):
            all_messages = []
            
            #Every list contains all the possible messages in that possition (inside de message secuence)
            all_messages.append(["Hi human!", "Hey human!", "I like your style human!"])
            all_messages.append (["I am a monster 😊, But a good one ☝"])
            all_messages.append (["I came from the Monsterland ", "I came to the Humanland "])
            all_messages.append (["to show humans the sounds we monsters do", "to show humans the sounds of monsters", "to show you the sounds of monsters", "to show you the sounds we monsters do"])
            all_messages.append (["Do you like DnB?, check my track!", "If you like trippy stuff, check out:", "I released this song with some cool animations 👇"])
            all_messages.append (["https://www.youtube.com/watch?v=U8Y_XPxr8g4&feature=youtu.be"])
            all_messages.append (["I hope you like it!", "I hope you enjoy!", "Enjoy!"])
            all_messages.append (["And have a great human day!", "And have a great human day! Or like we monsters say, GRROOOTHK!!! ❤️"])
            all_messages.append (["❤️", "👌", "🖖"])
            return self._select_one_message_for_each_row(all_messages)
            
            
        def _select_one_message_for_each_row(self, all_messages):
            resulting_list = []
            for row in all_messages:
                resulting_list.append(row[randint(0, len(row))-1])
            return resulting_list
                                          
            
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
#a_bot.unfollow_bastards(50)
a_bot.talk_to_fans_of("account_similar_to_yours", 4)
#print(a_bot._generate_messages())