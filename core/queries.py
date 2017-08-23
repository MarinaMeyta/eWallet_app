SQL_CREATE_PAYMENTS = '''
    CREATE TABLE IF NOT EXISTS payments(
      payment_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      user_id INT NOT NULL,
      date DATE NOT NULL,
      sum REAL NOT NULL,
      status INTEGER 
    );
'''

SQL_INSERT_PAYMENT = '''
    INSERT INTO payments (user_id, date, sum, status) VALUES (
        :user_id,
        :date,
        :sum,
        :status
    );
'''

SQL_SELECT_OUTCOMING = '''
    SELECT * FROM payments WHERE status=0;
'''

SQL_SELECT_INCOMING = '''
    SELECT * FROM payments WHERE status=1;
'''

SQL_GET_BALANCE = '''
    SELECT * FROM payments WHERE status=1;
'''