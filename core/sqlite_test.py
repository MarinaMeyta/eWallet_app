import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def getOrCreateDatabase(walletId, PIN):
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setHostName("localhost")
    db.setDatabaseName("walletdb")
    db.setPassword(PIN)
    db.setUserName(walletId)

    # opening connection
    db.open()
    sql = "SELECT *;"
    query = QSqlQuery(sql, db)
    query.exec()
    print(query.result())

    # finishing transaction
    db.commit()
    db.close()


if __name__ == '__main__':
    getOrCreateDatabase(sys.argv[1], sys.argv[2])