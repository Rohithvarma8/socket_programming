from socket import *

def problem_algo(question):
    type,operand1,operator,operand2 = question.split()
    operand1, operand2 = int(operand1), int(operand2)
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 // operand2 
    

def clientSocket():
    serverName = '127.0.0.1'
    serverPort = 8888
    with socket(AF_INET, SOCK_STREAM) as clientSocketTcp:
        try:
            clientSocketTcp.connect((serverName, serverPort)) # Making a TCP conn to server
            clientSocketTcp.settimeout(15)
            #welcome message (handshake)
            initialContact = clientSocketTcp.recv(1024).decode().strip()
            print("Server-side Message: " + initialContact) # message from server
            #sending husky name to server
            northeasternUsername = input("enter your username of Husky ID: ")
            greetServer = "HELLO " + northeasternUsername + "\n"
            print("sending... " + greetServer.strip() )
            clientSocketTcp.send(greetServer.encode())

            while True:
                query = clientSocketTcp.recv(1024).decode().strip()
                print("server: " + query)

                if query.startswith("DONE"):
                    print("Recevied Flag: " + query.split()[1])
                    break
                elif query.startswith("MATH"):
                    ans = problem_algo(query)
                    res = "ANSWER "+ str(ans) + "\n"
                    print("sending: " + res.strip())
                    clientSocketTcp.send(res.encode())
                elif not query:
                    print("No data received. Exiting.")
                    break

            clientSocketTcp.close()        


        except timeout:
            print("connection timeout")
        except ConnectionRefusedError:
            print("500 internal server error i think server is not running")
        except Exception as e:
            print("Error: " + e)    

    
    

if __name__ == "__main__":
    clientSocket()