import csv
import os
from Account import Account
class AccountTest:
    def __init__(self):
        self.filepath_test = "test/account_test_data/"
        self.name = "test_name"
        self.psw = "test_psw"
        self.proxy = "127.0.0.1:8080"
        
        
    def test_create_account(self):
        print("**** Testing create account ****")
        # Given
        self._create__test_csv()
        
        # When
        self.undertest = Account(self.filepath_test)
        
        # Then
        assert self.name == self.undertest.name
        assert self.psw == self.undertest.psw
        assert self.proxy == self.undertest.proxy
        
        # After test
        os.remove(self.filepath_test + Account.default_gen_data_file_name)
        print("**** Test successful ****")
    
    def test_create_account_without_proxy(self):        # Whithout proxy should be represented in the file with "None" String
        print("**** Testing create account without proxy****")
        # Given
        self.proxy = "None"
        self._create__test_csv()
        
        # When
        self.undertest = Account(self.filepath_test)
        
        # Then
        assert self.name == self.undertest.name
        assert self.psw == self.undertest.psw
        assert None == self.undertest.proxy
        
        # After test
        os.remove(self.filepath_test + Account.default_gen_data_file_name)
        print("**** Test successful ****")
        
    def _create__test_csv(self):
        with open(self.filepath_test + Account.default_gen_data_file_name, 'w', newline='') as csvfile:
            data = [['Name', 'Pass', 'Proxy'],
                    [self.name , self.psw, self.proxy]]
            writer = csv.writer(csvfile)
            writer.writerows(data)
        csvfile.close()
        
    def create__test_csv_with_data(self, name, psw, proxy):
        with open(self.filepath_test + Account.default_gen_data_file_name, 'w', newline='') as csvfile:
            data = [['Name', 'Pass', 'Proxy'],
                    [name , psw, proxy]]
            writer = csv.writer(csvfile)
            writer.writerows(data)
        csvfile.close()