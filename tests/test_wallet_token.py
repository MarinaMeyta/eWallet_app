import pytest
import shutil
import os
from wallet_token import Token


PATH_TO_TEST_TOKEN_1 = './token1/'
PATH_TO_TEST_TOKEN_2 = './token2/'
PIN = '878980'


@pytest.fixture(scope="module")
def token():
    os.makedirs(PATH_TO_TEST_TOKEN_1)
    os.makedirs(PATH_TO_TEST_TOKEN_2)
    token = Token(PIN, PATH_TO_TEST_TOKEN_1)
    yield token
    shutil.rmtree(PATH_TO_TEST_TOKEN_1)
    shutil.rmtree(PATH_TO_TEST_TOKEN_2)


def test_generate_id(token):
    assert token.id is not None


def test_generate_salt(token):
    assert token.salt is not None


def test_generate_hash(token):
    assert token.hash is not None


def test_saving_token(token):
    token.save(PATH_TO_TEST_TOKEN_2)


def test_import_token(token):
    imported_token = Token(PIN, PATH_TO_TEST_TOKEN_1)
    assert token.hash == imported_token.hash


def test_check_PIN(token):
    wrong_PIN = '4849'
    right_PIN = PIN
    assert token.check_PIN(wrong_PIN) is False
    assert token.check_PIN(right_PIN) is True
