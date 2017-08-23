import sys
from core import queries
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5 import QtGui


class WalletConnection():
    def __init__(self, PIN, DB_NAME):
        self.conn = self.init_connection(PIN, DB_NAME)
        self.query = QSqlQuery(self.conn)
        self.open()
        self.create_payments_table()
        self.close()

    def init_connection(self, PIN, DB_NAME):
        conn = QSqlDatabase.addDatabase("QSQLITE")
        conn.setHostName("localhost")
        conn.setDatabaseName(DB_NAME)
        conn.setPassword(PIN)
        return conn

    def open(self):
        return self.conn.open()

    def close(self):
        # finishing transactions
        self.conn.commit()
        return self.conn.close()

    def create_payments_table(self):
        return self.query.exec(queries.SQL_CREATE_PAYMENTS)

    def insert_payment(self, user_id, date, sum, status):
        self.query.prepare(queries.SQL_INSERT_PAYMENT)
        self.query.bindValue(':user_id', user_id)
        self.query.bindValue(':date', date)
        self.query.bindValue(':sum', sum)
        self.query.bindValue(':status', status)
        return self.query.exec_()

    def get_incoming_payments(self):
        return self.query.exec(queries.SQL_SELECT_INCOMING)

    def get_outcoming_payments(self):
        return self.query.exec(queries.SQL_SELECT_OUTCOMING)

    def get_balance(self):
        return self.query.exec(queries.SQL_GET_BALANCE)