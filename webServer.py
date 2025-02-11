d# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:
        print('Ready to serve...')
        connectionSocket, addr =  serverSocket.accept()

        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]

            f = open(filename[1:], "rb") 


            outputdata= b"HTTP/1.1 200 OK\r\n"
            outputdata+=b"Content-Type: text/html; charset=UTF-8\r\n"
            outputdata+=b"Server: PythonHTTPServer\r\n"
            outputdata+=b"Connection: close\r\n"
            outputdata+= b"\r\n"

            connectionSocket.sendall(outputdata)



            for i in f:  
                connectionSocket.sendall(i)

            connectionSocket.close()  # closing the connection socket

        except Exception as e:
            invalid_message = b"HTTP/1.1 404 Not Found\r\n"
            invalid_message += b"Content-Type: text/html; charset=UTF-8\r\n"
            invalid_message += b"Server: PythonHTTPServer\r\n"
            invalid_message += b"Connection: close\r\n"
            invalid_message += b"\r\n"
            invalid_message += b"<html><body><h1>404 Not Found</h1></body></html>"


            connectionSocket.sendall(invalid_message)
          

        connectionSocket.close()
    # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop.
    # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
    #serverSocket.close()
    # sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
