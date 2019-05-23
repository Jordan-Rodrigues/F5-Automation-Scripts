from f5.bigip import ManagementRoot

#Asks the user for the name of the server, and the username/password of the admin acct.
def serverReceiver():
    serverIP = input("Please enter the server IP: ")
    username = input("Please enter the admin username: ")
    password = input("Please enter the admin password: ")
    infoList = [serverIP, username, password]
    return infoList

def bigIPAuthenticator(infoList):
    try:
        bigIP = ManagementRoot(str(infoList[0]), str(infoList[1]), str(infoList[2]))
    except Exception as e:
        print("ERROR: SEE BELOW" + "\n" + "*" * 50 + "\n")
        print(str(e) + "\n" + "*" * 20 + "\n" + "\nPlease Enter the Credentials Again.")
        infoList = serverReceiver()
        bigIP = bigIPAuthenticator(infoList)
    finally:
        print("*" * 20)
    print("Connecting to the BIG IP was a success")
    return bigIP

infoList = serverReceiver()
bigIP = bigIPAuthenticator(infoList)
