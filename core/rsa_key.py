import os
from Crypto.PublicKey import RSA
from Crypto import Random


class RSAkey():
    def __init__(self, PIN, path):
        try:
            self.key = self.import_key(PIN, path)
        except IOError:
            os.makedirs(path, exist_ok=True)
            self.key = self.generate_key(PIN, path)


    def import_key(self, PIN, path):
        with open(os.path.join(path, 'privatekey.pem'), 'r') as key_file:
            try:
                key = RSA.importKey(key_file.read(), PIN)
            except:
                key = None
        return key


    def generate_key(self, PIN, path):
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        exported_key = key.exportKey('PEM', PIN, pkcs=1)
        with open(os.path.join(path, 'privatekey.pem'), 'wb') as outfile:
            outfile.write(bytes(exported_key))
        return key