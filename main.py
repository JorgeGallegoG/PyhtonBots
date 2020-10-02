# -*- coding: utf-8 -*-
from InstaBot import InstaBot
from test.AccountTest import AccountTest
from test.DataTest import DataTest
from Data import Data
from time import sleep
import os
import ray

"""
*  Test set, uncomment and execute to run all tests
"""

"""
account_test = AccountTest()
account_test.test_create_account()
account_test.test_create_account_without_proxy()

data_test = DataTest()
data_test.test_white_list_save_and_load()
data_test.test_add_elem_to_temp_followeds()
data_test.test_add_two_elem_to_temp_followeds()
"""


"""
*  Create csv data file
"""

"""
account_test = AccountTest()
account_test.create__test_csv_with_data("", "", "None")
"""


"""
*  Parallel processing execution (one method for every account)
"""
@ray.remote
def execute_happy_monster():
    happymonster_bot = InstaBot("accounts/happymonster/")
    happymonster_bot.talk_to_fans_of("account_to_anchor", 49)
 
@ray.remote
def execute_heyhabibi():
    habibi_botbot = InstaBot("accounts/heeyhabibi/")
    habibi_botbot.talk_to_fans_of("account_to_anchor2", 58)
    
ray.init()
all_ops = []
all_ops.append(execute_happy_monster.remote())
all_ops.append(execute_heyhabibi.remote())
ray.get(all_ops)

"""
**  SET UP NEW ACCOUNT GUIDE
**  Hire proxy and Authorise by IP
**  Create a folder with the name of the account inside the folder Accounts
**  Inside this folder copy and edit the gen_data file from other account folder
**  Modify gen_data file writing the user name pass and proxy of the account,
**  if you are going to use your IP then leave that value to None
**  Create a folder with name "data" inside the created folder
**  Copy inside this data folder the file "conversation.csv" from other account folder
**  Edit conversation file to adjust it to the new account
**  Make a first execution of the InstaBot for this account and then execute a generation of
**  the white list
**  
"""
"""
habibi_botbot = InstaBot("accounts/heeyhabibi/")
habibi_botbot.generate_white_list()
"""

"""
*  Single execution example
"""
#happymonster_bot = InstaBot("accounts/happymonster/")
#a_bot.try_talk_until_success("", 100)
#a_bot.try_unfollow_bastards_until_success(74)