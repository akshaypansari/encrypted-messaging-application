from socket import *
serverPort = 5050
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
count = 0
while 1:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024)
    print(sentence, count)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
    count += 1