import crypt
import sys

def get_password_hash(password):
    salt = crypt.mksalt(crypt.METHOD_SHA512)
    hash = crypt.crypt(password, salt)
    print("password: ", password)
    print("salt: ", salt)
    print("hash: ", hash)

if __name__ == '__main__':
    get_password_hash(sys.argv[1])