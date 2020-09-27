"""
*  TempFollowed is an object that contains a list with names of followed contacts
*  In the proccess of following/talking to people this list is generated with names of the followed contacts 
*  The other attribute is an identifier composed by the time and date when the execution started
"""
import datetime
class TempFollowed:
    def __init__(self):
        self.__date = datetime.date
        self.__time = datetime.time
        self.__list_followed = None
    
    def set_list_followed(self, lis):
        self.__list_followed = lis
        
    def get_list_followed(self):
        return self.__list_followed