
import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from Crypto.PublicKey import RSA
from Crypto import Random
import os.path
import settings



'''
EnterPIN

if Token does not exits:
    make Token(PIN):
        make hash(PIN, salt)
        save Token to json file  
    make RSA using token.hash
else:
    read token from file and check hash(PIN) 
    check token
    if PIN is correct: -> WorkWithProgram
    else: 
        user message "Try again"
        goto EnterPIN
   
        
WorkWithProgram:
    if db exists:
        connect to db with RSA key
        get payment data -> UI 
    else:
        create db
        set password with RSA key

'''


class Wallet():
    def __init__(self, PIN, parent=None):
        self.db_connection = self.create_db_connection()
        self.rsa_key = self.get_or_generate_rsa(PIN)
        self.token = self.get_or_generate_token(PIN)

    def get_or_generate_rsa(self, PIN):
        if not os.path.exists(os.path.join(settings.PATH_TO_KEYS, 'privatekey.pem')):
            random_generator = Random.new().read
            key = RSA.generate(1024, random_generator)
            exported_key = key.exportKey('PEM', PIN, pkcs=1)

            with open(os.path.join(settings.PATH_TO_KEYS, 'privatekey.pem'), 'wb') as outfile:
                outfile.write(bytes(exported_key))

            return key
        else:
            return self.import_key(PIN)

    def import_rsa(self, PIN):
        with open(os.path.join(settings.PATH_TO_KEYS, 'privatekey.pem'), 'r') as infile:
            key = RSA.importKey(infile.read(), PIN)
        return key


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

