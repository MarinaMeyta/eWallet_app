import os
import settings
from Crypto.PublicKey import RSA
from Crypto import Random


class RSAkey():
    def __init__(self, PIN):
        try:
            with open(os.path.join(settings.PATH_TO_KEYS, 'privatekey.pem')) as key_file:
                self.key = self.import_key(PIN)
        except IOError:
            self.key = self.generate_key(PIN)


    def import_key(self, PIN):
        with open(os.path.join(settings.PATH_TO_KEYS, 'privatekey.pem'), 'r') as infile:
            try:
                key = RSA.importKey(infile.read(), PIN)
            except:
                key = None
        return key


    def generate_key(self, PIN):
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        exported_key = key.exportKey('PEM', PIN, pkcs=1)
        with open(os.path.join(settings.PATH_TO_KEYS, 'privatekey.pem'), 'wb') as outfile:
            outfile.write(bytes(exported_key))
        return key