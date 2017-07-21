from Crypto.PublicKey import RSA 
from Crypto import Random

random_generator = Random.new().read
PIN = "456431"
private_key = RSA.generate(2048, random_generator) 
exported_key = private_key.exportKey('PEM', PIN, pkcs=1)
f = open('privatekey.pem','wb')
f.write(bytes(exported_key)) 
f.close()


f = open('privatekey.pem','r')
key = RSA.importKey(f.read(), PIN)
pub_key = key.publickey()
print(pub_key)

if private_key == key:
    print("True") 
