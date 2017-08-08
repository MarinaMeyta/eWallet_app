import crypt
import sys
from hmac import compare_digest as compare_hash

def get_password_hash(password):
    salt = crypt.mksalt(crypt.METHOD_SHA512)
    hash = crypt.crypt(password, salt)
    print("password: ", password)
    print("salt: ", salt)
    print("hash: ", hash)

    login = compare_hash(crypt.crypt(password, hash), hash)
    print(login)

if __name__ == '__main__':
    get_password_hash(sys.argv[1])