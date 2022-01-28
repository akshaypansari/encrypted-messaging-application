import os
from jnius import autoclass

# first_java_line = 'javac Crypto.java'
# second_java_line = 'jar -cf Crypto.jar Crypto.class'
# os.system(first_java_line)
# os.system(second_java_line)

os.environ['CLASSPATH']="Crypto.jar"
crypt=autoclass("Crypto")
generateKeyPair = crypt.generateKeyPair()

publicKey = generateKeyPair.getPublic().getEncoded()
privateKey = generateKeyPair.getPrivate().getEncoded()
publicKey = publicKey.tostring()
privateKey = privateKey.tostring()
print(publicKey, type(publicKey))
# print(type(publicKeys))
encryptedData = crypt.encrypt(publicKey,"hi there".encode())
decryptedData = crypt.decrypt(privateKey, encryptedData)

# print(type(publicKey))
print((encryptedData.tostring()).decode())
# public_key = "pubkey".encode()
# print(type(public_key))
# print(publicKey + "234")

