# socket udp client em python
from socket import *

#definir o nome do host e a porta do servidor
serverName = 'hostname'
serverPort = 12000

#datagrama do cliente
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print (modifiedMessage)

clientSocket.close()


#socket udp servidor

#from socket import *
#serverport = 12000
#serverSocket = socket(AF_INET, SOCK_DGRAM)
#serverSocket.bind(('', serverPort))
#print ("the server is ready to recieve") 
#while 1:
#    message, clientAdress = serverSocket.recvfrom(2048)
#    modifiedMessage = message.upper()
#    serverSocket.sendto(modifiedMessage, clientAdress)


    #socket tcp
    #from socket import *
    #serverName = 'servername'
    #serverPort = 12000
    #clientSocket = socket(AF_INET, SOCK_STREAM)
    #clientSocket.connect((serverName, serverPort))
    #sentence = input('Input lowercase sentence:')
    #clientSocket.send(sentence)
    #modifiedSentence = clientSocket.recv(1024)
    #print("from server:", modifiedSentence)
    #clientSocket.close()

    #tcp servidor
    # from socket import *
    #serverPort = 12000
    #serverSocket = socket(AF_INET, SOCK_STREAM)
    #serverSocket.bind(('', serverPort))
    #serverSocket.listen(1)
    #print('the server is ready to recieve')
    #while 1:
        #connectionSocket, addr = serverSocket.accept()