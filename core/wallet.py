
import sys
import json


import os.path
import settings
from PyQt5.QtSql import QSqlDatabase, QSqlQuery



class Wallet():
    def __init__(self, rsa_key, parent=None):
        self.db_connection = self.create_db_connection(rsa_key)


    def get_outcome_payments(self):
        pass


    def get_income_payments(self):
        pass


    def create_db_connection(self, password):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setHostName("localhost")
        db.setDatabaseName("walletdb")
        db.setPassword(password)
        return db.connectionName()




class Payment():
    def __init__(self, amount, date, parent=None):
        self.amount = amount
        self.date = date

    def save(self):
        pass

