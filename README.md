# Ecrypted Messaging Application
A chat application developed as part of course assignment of Computer Networks. It allows users to do an encrypted chat with one another, which cannot be decrypted by the chat server.

## Prerequisites
Java
Pyjnius
Crypto.jar

## Installing
Installation of Pyjnius : https://pyjnius.readthedocs.io/en/stable/installation.html

Creating Crypto.jar:
    javac Crypto.java
    jar -cf Crypto.jar Crypto.class 

## Running
To run unencrypted version:
	cd src/unencrypted
	Start Server : python3 server.py "port"
	Start a client : python3 client.py "username" "server_ip" "server_port"

To run unencrypted version:
	cd src/encrypted
	Start Server : python3 server.py "port"
	Start a client : python3 client.py "username" "server_ip" "server_port"


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details