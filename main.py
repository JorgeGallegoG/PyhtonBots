# -*- coding: utf-8 -*-
from InstaBot import InstaBot
from test.AccountTest import AccountTest

"""
*  Test set, uncomment and execute to run all tests
"""

"""
account_test = AccountTest()
account_test.test_create_account()
account_test.test_create_account_without_proxy()
"""

"""
*  Create csv data file
"""

"""
account_test = AccountTest()
account_test.create__test_csv_with_data("", "", "None")
"""



#Execution

habibi_bot = InstaBot("accounts/heeyhabibi")
happymonster_bot = InstaBot("accounts/happymonster")
#a_bot = InstaBot('heeyhabibi', 'eskipiskipuski', "5.188.181.95:45785")
#a_bot = InstaBot('happy_monster_music', 'ElMounstro51')
#a_bot.talk_to_fans_of("subfocus", 20)
#a_bot.try_talk_until_success("dawnwall", 100)
#a_bot.try_unfollow_bastards_until_success(74)
#a_bot.unfollow_bastards(20)
#a_bot.talk_to_fans_of("ola", 20)
#print(a_bot._generate_messages())