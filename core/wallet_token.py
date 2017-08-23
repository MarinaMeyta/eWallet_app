import crypt
import json
import os
import string
import random
from hmac import compare_digest as compare_hash


class Token():
    def __init__(self, PIN, path):
        try:
            with open(os.path.join(path, 'TOKEN')) as token_file:
                data = json.load(token_file)
                self.id = data["id"]
                self.salt = data['salt']
                self.hash = data['hash']
        except IOError:
            os.makedirs(path, exist_ok=True)
            self.id = self.generate_id()
            self.salt = self.generate_salt(PIN)
            self.hash = self.generate_hash(PIN, self.salt)
            self.save(path)

    def generate_id(self):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))

    def generate_salt(self, PIN):
        return crypt.mksalt(crypt.METHOD_SHA512)

    def generate_hash(self, PIN, salt):
        return crypt.crypt(PIN, salt)

    def save(self, path):
        with open(os.path.join(path, 'TOKEN'), 'w') as hash_file:
            data = {'id': self.id, 'salt': self.salt, 'hash': self.hash}
            json.dump(data, hash_file, sort_keys=True, indent=4)

    def check_PIN(self, PIN):
        return compare_hash(crypt.crypt(PIN, self.hash), self.hash)