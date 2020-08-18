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
            
            self._log_in(username, pw)
            self._passing_not_nows()
        #Constants    
        _following_path = ".\data"
        _following_file_name = "following"
        
        #Global variables
        mofos = None
        unfollowed = 0
        
        
        def _log_in(self, username, password):
            self._human_sleep(2)
            self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(password)
            self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
                .click()
            self._human_sleep(4)
            
        '''
        Click and close the messages that appear when entering the app for the first time
        '''
        def _passing_not_nows(self):
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
            self._human_sleep(4)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
          
        '''
        Returns a list with the accounts that you follow but don´t follow you (following - followed)
        '''
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
            #Check if is the first execution (otherwise we have the list generated)
            if self.mofos == None:
                self.mofos = self.get_unfollowers()
                print("**** Created list of bastards who didn´t follow you back ****", flush=True)
            self._human_sleep(4)
            self.driver.find_element_by_xpath("//a[contains(@href, 'following')]")\
                .click()
            self._human_sleep(2)
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
            self._load_all_contacts(scroll_box)
            #self._human_sleep(10*61)
            self.iterate_list_of_unfollowers(n)
        
        """
        Navigates through the list of of unfollowers and stops following n accounts
        """
        def iterate_list_of_unfollowers(self, n):
            m = n
            
            while n > 0:
                self._take_naps(n)
                self._human_sleep(2)
                
                #if multiple executions we don´t want to go through the entire list again, so we skip those contacts already unfollowed
                name_to_unfollow = self.mofos[m-n+self.unfollowed]
                elem_name_to_unfollow = self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(name_to_unfollow))
                antecesor_of_unfollowed = self._find_ancestor(5, elem_name_to_unfollow) 
                button_of_unfollowed = antecesor_of_unfollowed.find_element_by_xpath(".//button[contains(text(), 'Following')]")
                self._human_sleep(5)
                button_of_unfollowed.click()
                print("**** Stopped following " + name_to_unfollow + " ****")
                self._human_sleep(2)
                self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]")\
                    .click()
                self._human_sleep_slow(3)
                n-=1
            self.unfollowed += m
            
        #TODO Unspaguetti code yeah :)       
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
                changed_scroll_flag = False
                x = 0
                while x < n_of_fans:
                #for x in range(n_of_fans):
                    #self._take_naps(x)
                    #When we are accesing this manu from the "previous page function" the xpath of the scroll box is changed
                    if changed_scroll_flag == True: 
                        scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]")
                    self._human_sleep(2)
                    flag = False
                    while flag == False:
                        self._human_sleep(4)
                        try:
                            button_to_follow = scroll_box.find_element_by_xpath(".//button[text()='Follow']")
                            flag = True
                        #if there is no contact to follow loaded keep scrolling
                        except NoSuchElementException:
                            self.driver.execute_script("""
                                                       arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                                       return arguments[0].scrollHeight;
                                                   """, scroll_box)
                            self._human_sleep(3)
                            
                            #scroll 2 times to be sure it does not get stuck
                            self.driver.execute_script("""
                                                       arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                                       return arguments[0].scrollHeight;
                                                   """, scroll_box)
                            self._human_sleep(3)
                            continue
                    button_to_follow.click()
                    self._human_sleep(3)
                    
                    antecesor = self._find_ancestor(3, button_to_follow)
                    list_name_of_followed_b = antecesor.find_elements_by_tag_name('a')
                    temp_list_names_of_followed_text = [name.text for name in list_name_of_followed_b if name.text != '']
                    name_of_followed = antecesor.find_element_by_xpath(".//a[@href]")
                    try:
                        button_followed = antecesor.find_element_by_xpath(".//button[contains(text(), 'Following')]")
                        name_of_followed.click()
                        self._human_sleep(3)
                        print(temp_list_names_of_followed_text[0])
                        x =+ 1
                        followed_list.extend(temp_list_names_of_followed_text)
                        self.driver.find_element_by_xpath("//button[contains(text(), 'Message')]")\
                        .click()
                        self._human_sleep(3)
                        
                        #When we are accesing this manu from the "previous page function" the xpath of the scroll box is changed
                        changed_scroll_flag = True
                        try:
                            #do not writte if there are already messages in the conversation (cause you already talked with this person
                            already_written = self.driver.find_element_by_xpath('//div[@class="iXTil   "]')
                        except NoSuchElementException:
                            self._send_messages()
                            self._human_sleep_fast(2)
                        self.driver.execute_script("window.history.go(-1)")
                        self._human_sleep(3)
                        self.driver.execute_script("window.history.go(-1)")
                    except NoSuchElementException:
                        pass
                        
                    self._human_sleep(1)
                    temp_list_names_of_followed_text = []
                    self._human_sleep(3)
                    
                with open (self._following_path + self._following_file_name + ".csv",'a') as following_file:
                    writer = csv.writer(following_file, dialect='excel')
                    writer.writerow(followed_list)
                    self._human_sleep(3)
                    self.driver.execute_script("window.history.go(-1)")
                    self._human_sleep(1)
                    self.driver.execute_script("window.history.go(-1)")
                    self._human_sleep(1)
                    self.driver.execute_script("window.history.go(-1)")
               
        def _send_messages(self):
            list_messages = self._generate_messages()
            self._human_sleep(5)
            print("**** Sending Messages ****")
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
        #TODO read a file with the messages instead of harcoding here
        def _generate_messages(self):
            print("**** Setting messages ****")
            all_messages = []
            
            #Every list contains all the possible messages in that possition (inside de message secuence)
            all_messages.append(["Hi human!", "Hey human!", "I like your style human!"])
            #all_messages.append (["I am a monster 😊, But a good one ☝"])
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
            print("**** Finding antecesor of element " + element.text + " ****")
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
            
        #TODO use a randomizer instead of this harcoding
        def _take_naps(self, n):
            if n == 10:
                print("**** napping 3 min ****", flush=True)
                sleep(60*3)
            if n == 17:
                print("**** napping 5 min ****", flush=True)
                sleep(52*5)
            if n == 25:
                print("**** napping 1 min ****", flush=True)
                sleep(55*1)
            if n == 33:
                print("**** napping 9 min ****", flush=True)
                sleep(60*9)
            if n == 40:
                print("**** napping 11 min ****", flush=True)
                sleep(49*11)
            if n == 48:
                print("**** Napping 2 min ****", flush=True)
                sleep(56*2)
            if n == 53:
                print("**** Napping 3 h ****", flush=True)
                sleep(56*62*3)
                            
#TODO write the pass in a file and read it from there
a_bot = InstaBot('account', 'pass')
a_bot.unfollow_bastards(65)
#a_bot.talk_to_fans_of("account_to_shadow", 50)
#print(a_bot._generate_messages())