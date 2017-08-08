from Crypto.PublicKey import RSA 
from Crypto import Random

random_generator = Random.new().read
PIN = "456431"
public_key = RSA.generate(1024, random_generator)
print("public key: ", public_key)
exported_key = public_key.exportKey('PEM', PIN, pkcs=1)
exported_key_id = public_key.exportKey('PEM', pkcs=1)
f = open('expotedkey.pem','wb')
f.write(bytes(exported_key)) 
f.close()

f = open('expotedkey_id.pem','wb')
f.write(bytes(exported_key_id))
f.close()

f = open('privatekey.pem','r')
key = RSA.importKey(f.read(), PIN)
pub_key = key.publickey()
exported_key = pub_key.exportKey('PEM')
f = open('pubkey.pem','wb')
f.write(bytes(exported_key)) 
f.close()




if public_key == key:
    print("True") 

