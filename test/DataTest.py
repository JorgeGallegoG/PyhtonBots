from Data import Data
import os
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