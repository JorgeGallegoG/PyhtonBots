# -*- coding: utf-8 -*-
from selenium import webdriver
import pickle
import csv
"""
Created on Wed Sep  10 1:56:45 2020

@author: Jorge
"""

"""
*  This class contains all the information about the account that holds it
*  This information will be stored always in files inside the account directory,
*  under it's own directory with default name data, serialized and deserialized to the 
*  instanciated objects of this class when required.
"""
class Data:
    
    default_subdirectory_name = "data/"
    default_conversation_filename = "conversation.csv"
    
    def __init__(self, account_path):
        self.account_path = account_path #Reference to the account holding the Data object
        self.gen_data = []
        self.whitelist = []
        self.unfollowers = []
        self.conversation = []
    
    def serialize_file(self, lis, file_name):
        file = open(self.account_path + '/' + self.default_subdirectory_name + file_name, 'wb') 
        pickle.dump(lis, file)
        file.close()
        
    def deserialize_file(self, file_name):
        file = open(self.account_path + '/' + self.default_subdirectory_name + file_name, 'rb') 
        deserialized = pickle.load(file)
        file.close()
        return deserialized
    
    def csv_to_list(self, file_name):
        with open(file_name, newline='') as file:
            reader = csv.reader(file)
            return list(reader)
        
    def load_conversation(self):
        self.conversation = self.csv_to_list(self.default_conversation_filename)