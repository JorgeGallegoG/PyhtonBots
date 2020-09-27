# -*- coding: utf-8 -*-
from InstaBot import InstaBot
from test.AccountTest import AccountTest
from test.DataTest import DataTest
from Data import Data
from time import sleep

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



#Execution
"""
habibi_bot = InstaBot("accounts/heeyhabibi")
"""

#EXECUTION GOOD

happymonster_bot = InstaBot("accounts/happymonster/")
#happymonster_bot.unfollow_bastards(85)
happymonster_bot.talk_to_fans_of("aaa", 100)


"""
data = Data("accounts/jeje")
#lis1 = [["asd"], ["hehehe"]]
lis1 = data.deserialize_file("test")
print(lis1[0])
print(lis1[1])
"""



#a_bot = InstaBot('heeyhabibi', 'eskipiskipuski', "5.188.181.95:45785")
#happymonster_bot = InstaBot("accounts/happymonster")

#a_bot.talk_to_fans_of("", 20)
#a_bot.try_talk_until_success("", 100)
#a_bot.try_unfollow_bastards_until_success(74)
#a_bot.unfollow_bastards(20)
#a_bot.talk_to_fans_of("ola", 20)
#print(a_bot._generate_messages())