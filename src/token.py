import uuid
import crypt
import json
from hmac import compare_digest as compare_hash


class Token():
    def __init__(self, PIN):
        self.id = self.generate_id()
        self.salt = self.generate_salt(PIN)
        self.hash = self.generate_hash(PIN, self.salt)
        self.save()

    def generate_id(self):
        return uuid.uuid4().hex

    def generate_salt(self, PIN):
        return crypt.mksalt(crypt.METHOD_SHA512)

    def generate_hash(self, PIN, salt):
        return crypt.crypt(PIN, salt)

    def save(self):
        with open('TOKEN', 'w') as hash_file:
            data = {'id': self.id, 'salt': self.salt, 'hash': self.hash}
            json.dump(data, hash_file, sort_keys=True, indent=4)

    def check_PIN(self, PIN):
        return compare_hash(crypt.crypt(PIN, self.hash), self.hash)