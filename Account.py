import csv
from Data import Data

"""
*  The account has associated a filepath, this file contains 2 rows, the second one will be read, it has the name, pass and proxy,
*  if the proxy is None (String) it will be converted to None (value)
"""
class Account:
    
    default_gen_data_file_name = "gen_data.csv"
    
    def __init__(self, filepath):
        self.path = filepath
        data_list = self.load_gen_data()
        self.name = data_list[0]
        self.psw = data_list[1]
        if data_list[2] == "None":
            self.proxy = None
        else:
            self.proxy = data_list[2]
        self.data = Data(filepath)
        
    """
    ** The loaded data will be done from a file with path and name filepath and has the titles in the first row, values in the second 
    """
    def load_gen_data(self):
        print("oppening: " + self.path + self.default_gen_data_file_name)
        with open(self.path + self.default_gen_data_file_name) as csvfile:
            filereader = csv.reader(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            lis = [row for row in filereader]
            return lis[1]
        csvfile.close()
