# -*- coding: utf-8 -*-
from selenium import webdriver
import pickle
import csv
from time import sleep
import codecs
from TempFollowed import TempFollowed
"""
Created on Wed Sep  10 1:56:45 2020

@author: Jorge
"""

"""
*  This class contains all the information about the account that holds it
*  This information will be stored always in files inside the account directory,
*  under it's own directory with default name data, serialized and deserialized to the 
*  instanciated objects of this class when required.
*
*  temp_followeds contains an array of TempFollowed, lists that are generated when the follow and talk interactions happen
*  there is one list for every execution
"""
class Data:
    
    default_subdirectory_name = "data/"
    default_conversation_filename = "conversation.csv"
    default_temp_followeds = "temp_followeds.pkl"
    default_whitelist_filename = "white"
    
    def __init__(self, account_path):
        self.account_path = account_path #Reference to the account holding the Data object
        self.gen_data = []
        self.whitelist = []
        self.unfollowers = []
        self.__temp_followeds = None
        self.__conversation = []
        
    # Getters & Setters
    def get_white_list(self):
        return self.whitelist
    def get_temp_followeds(self):
        return self.__temp_followeds
    
    def set_temp_followeds(self, temp_followeds):
        self.__temp_followeds = temp_followeds
    
    def get_conversation(self):
        return self.__conversation
        
    def inicialize_data(self):
        print("**** Inicializing data of " + self.account_path + " ****")
        self.load_conversation()
        self.load_temp_followeds()
        self.load_white_list()
    
    def check_out_list(self):
        if self.__temp_followeds == None:
            self.load_temp_followeds()
        for temp_followed in self.__temp_followeds:
            print("List ")
            print(str(temp_followed.get_time()))
            print("**** :) ****")
            for name in temp_followed.get_list_followed():
                print(name)
                
    def save_temp_followeds(self):
        print((self.__temp_followeds[0]).get_list_followed()[0])
        self.serialize_file(self.__temp_followeds, self.default_temp_followeds)
        
    def load_temp_followeds(self):
        try:
            self.__temp_followeds = self.deserialize_file(self.default_temp_followeds)
        except FileNotFoundError:
            return None
    
    """
    *  Passing a list as argument, it creates a new TempFollowed objet to store that list and adds it to temp followeds
    """
    def add_elem_to_temp_followeds(self, lis):
        temp_followed = TempFollowed()
        temp_followed.set_list_followed(lis)
        if self.__temp_followeds == None:
            print("**** default_temp_followeds not loaded, will try to load****")
            self.load_temp_followeds()
            if self.__temp_followeds == None:
                print("**** Could not load default_temp_followeds will create one****")
                self.__temp_followeds = [temp_followed]
                return
        self.__temp_followeds.append(temp_followed)
    
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
        print("**** Loading conversation ****")
        self.__conversation = self.csv_to_list(self.account_path + self.default_subdirectory_name + self.default_conversation_filename)
    
    def save_white_list(self, lis):
        self.serialize_file(lis, self.default_whitelist_filename)
        
    def load_white_list(self):
        print("**** Loading whitelist")
        try:
            self.whitelist = self.deserialize_file(self.default_whitelist_filename)
        except FileNotFoundError:
            self.whitelist = None
                        
    
    """
    *  Having a list of lists removes all the empty elements in every sublist
    """
    def remove_empties(self, lis):
        reslist = []
        for line in lis:
            reslist.append([x for x in line if x!= ''])
        return reslist