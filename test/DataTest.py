from Data import Data
import os
from TempFollowed import TempFollowed
"""
Created on Wed Sep  13 6:06:45 2020

@author: Jorge
"""
class DataTest:

    def __init__(self):
        self.test_path = "test/account_test_data/"
        self.undertest = Data(self.test_path)

    
    def test_white_list_save_and_load(self):
        print("**** Test save and load white list ****")
        # Given
        e1 = "elem1"
        e2 = "elem2"
        e3 = "elem3"
        e4 = "elem4"
        lis = [e1, e2, e3, e4]
        
        # When
        self.undertest.save_white_list(lis)
        loaded_list = self.undertest.load_white_list()
        
        #Then
        assert loaded_list[0] == e1
        assert loaded_list[1] == e2
        assert loaded_list[2] == e3
        assert loaded_list[3] == e4
        
        # After test
        os.remove(self.test_path + self.undertest.default_subdirectory_name + self.undertest.default_whitelist_filename)
        print("**** Test successful ****")
        
    def test_add_elem_to_temp_followeds(self):
        print("**** Test add elem to temp followeds ****")
        # Given
        e1 = "elem1"
        e2 = "elem2"
        e3 = "elem3"
        e4 = "elem4"
        lis = [e1, e2, e3, e4]
        a_temp_followed = TempFollowed()
        a_temp_followed.set_list_followed(lis)
        
        # When
        self.undertest.add_elem_to_temp_followeds(a_temp_followed)
        
        # Then
        temp_followeds_in_data = self.undertest.get_temp_followeds()
        tested_list = temp_followeds_in_data[0].get_list_followed()
        assert len(temp_followeds_in_data) == 1 
        assert tested_list[0] == e1
        assert tested_list[1] == e2
        assert tested_list[2] == e3
        assert tested_list[3] == e4
        print("**** Test successful ****")
        self.undertest.set_temp_followeds(None)
        
    def test_add_two_elem_to_temp_followeds(self):
        print("**** Test add elem to temp followeds with two temp followeds****")
        # Given
        e1 = "elem1"
        e2 = "elem2"
        e3 = "elem3"
        e4 = "elem4"
        lis = [e1, e2]
        lis2 = [e3, e4]
        a_temp_followed = TempFollowed()
        a_temp_followed.set_list_followed(lis)
        a_temp_followed2 = TempFollowed()
        a_temp_followed2.set_list_followed(lis2)
        
        # When
        self.undertest.add_elem_to_temp_followeds(a_temp_followed)
        self.undertest.add_elem_to_temp_followeds(a_temp_followed2)
        
        # Then
        temp_followeds_in_data = self.undertest.get_temp_followeds()
        tested_list = temp_followeds_in_data[0].get_list_followed()
        tested_list2 = temp_followeds_in_data[1].get_list_followed()
        assert len(temp_followeds_in_data) == 2 
        assert tested_list[0] == e1
        assert tested_list[1] == e2
        assert tested_list2[0] == e3
        assert tested_list2[1] == e4
        print("**** Test successful ****")
        self.undertest.set_temp_followeds(None)
        
    def test_save_and_load_followeds(self):
        print("**** Test add elem to temp followeds with two temp followeds****")
        # Given
        e1 = "elem1"
        e2 = "elem2"
        e3 = "elem3"
        e4 = "elem4"
        lis = [e1, e2]
        lis2 = [e3, e4]
        a_temp_followed = TempFollowed()
        a_temp_followed.set_list_followed(lis)
        a_temp_followed2 = TempFollowed()
        a_temp_followed2.set_list_followed(lis2)
        
        # When
        self.undertest.add_elem_to_temp_followeds(a_temp_followed)
        self.undertest.add_elem_to_temp_followeds(a_temp_followed2)
        self.undertest.save_temp_followeds()
        self.undertest.set
        
        # Then
        temp_followeds_in_data = self.undertest.get_temp_followeds()
        tested_list = temp_followeds_in_data[0].get_list_followed()
        tested_list2 = temp_followeds_in_data[1].get_list_followed()
        assert len(temp_followeds_in_data) == 2 
        assert tested_list[0] == e1
        assert tested_list[1] == e2
        assert tested_list2[0] == e3
        assert tested_list2[1] == e4
        print("**** Test successful ****")
        self.undertest.set_temp_followeds(None)
        