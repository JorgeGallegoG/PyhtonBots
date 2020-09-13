# -*- coding: utf-8 -*-
from selenium import webdriver
import pickle
import csv
from time import sleep
import codecs
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
    default_whitelist_filename = "white"
    
    def __init__(self, account_path):
        self.account_path = account_path #Reference to the account holding the Data object
        self.gen_data = []
        self.whitelist = []
        self.unfollowers = []
        self.conversation = []
        self.inicialize_data()
        
    def inicialize_data(self):
        self.load_conversation()
    
    """
    *  Serializes a list into the path indicated in the Account containing this data object, inside the default subdirectory
    """
    def serialize_file(self, lis, file_name):
        file = open(self.account_path + self.default_subdirectory_name + file_name, 'wb') 
        pickle.dump(lis, file)
        file.close()
        
    """
    *  Deserializes a list in the path indicated in the Account containing this data object, inside the default subdirectory
    """
    def deserialize_file(self, file_name):
        file = open(self.account_path + self.default_subdirectory_name + file_name, 'rb') 
        deserialized = pickle.load(file)
        file.close()
        return deserialized
    
    def csv_to_list(self, file_name):
        reader = csv.reader(codecs.open(file_name, 'rU', 'utf-16'))
        lis = list(reader)
        return self.remove_empties(lis)
        
    def load_conversation(self):
        self.conversation = self.csv_to_list(self.account_path + self.default_subdirectory_name + self.default_conversation_filename)
    
    def save_white_list(self, lis):
        self.serialize_file(lis, self.default_whitelist_filename)
                        
    
    """
    *  Having a list of lists removes all the empty elements in every sublist
    """
    def remove_empties(self, lis):
        reslist = []
        for line in lis:
            reslist.append([x for x in line if x!= ''])
        return reslist