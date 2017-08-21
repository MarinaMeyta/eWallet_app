import pytest
import test_settings
from rsa_key import RSAkey


@pytest.fixture(scope="module")
def key():
    key = RSAkey(test_settings.PIN, test_settings.PATH_TO_TEST_KEY)
    return key


def test_import_key(key):
    assert key.import_key(test_settings.PIN, test_settings.PATH_TO_TEST_KEY) is not None
    assert key.import_key(test_settings.WRONG_PIN, test_settings.PATH_TO_TEST_KEY) is None


def test_generate_key(key):
    assert key.generate_key(test_settings.PIN, test_settings.PATH_TO_TEST_KEY) is not None