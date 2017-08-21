import pytest
import shutil
import os
import test_settings
from wallet_token import Token


@pytest.fixture(scope="module")
def token():
    os.makedirs(test_settings.PATH_TO_TEST_TOKEN_1)
    os.makedirs(test_settings.PATH_TO_TEST_TOKEN_2)
    token = Token(test_settings.PIN, test_settings.PATH_TO_TEST_TOKEN_1)
    yield token
    shutil.rmtree(test_settings.PATH_TO_TEST_TOKEN_1)
    shutil.rmtree(test_settings.PATH_TO_TEST_TOKEN_2)


def test_generate_id(token):
    assert token.id is not None


def test_generate_salt(token):
    assert token.salt is not None


def test_generate_hash(token):
    assert token.hash is not None


def test_saving_token(token):
    token.save(test_settings.PATH_TO_TEST_TOKEN_2)


def test_import_token(token):
    imported_token = Token(test_settings.PIN, test_settings.PATH_TO_TEST_TOKEN_1)
    assert token.hash == imported_token.hash


def test_check_PIN(token):
    assert token.check_PIN(test_settings.WRONG_PIN) is False
    assert token.check_PIN(test_settings.PIN) is True
