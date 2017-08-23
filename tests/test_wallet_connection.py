import os
import test_settings
from core.wallet_connection import WalletConnection


def test_wallet_connection():
    db = WalletConnection(test_settings.PIN, test_settings.WALLET_ID)
    assert db.open() is True
    assert db.insert_payment(user_id='74849', date='9.09.17', sum=378, status='0') is True
    assert db.create_payments_table() is True
    assert db.get_incoming_payments() is True
    assert db.get_outcoming_payments() is True
    assert db.get_balance() is True
    db.close()
    assert db.conn.isOpen() is False
    os.remove(test_settings.WALLET_ID)
