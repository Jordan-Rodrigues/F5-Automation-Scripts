from f5.bigip import ManagementRoot

#Asks the user for the name of the server, and the username/password of the admin acct.
def serverReceiver():
    serverIP = input("Please enter the server IP: ")
    username = input("Please enter the admin username: ")
    password = input("Please enter the admin password: ")
    infoList = [serverIP, username, password]
    return infoList

#Attempts to make a connection to the BIG IP
def bigIPAuthenticator(infoList):
    try:
        bigIP = ManagementRoot(str(infoList[0]), str(infoList[1]), str(infoList[2]))
        print("Connecting to the BIG IP was a success\n" + "*" * 50)
    except Exception as e:
        print("\nERROR: SEE BELOW" + "\n" + "*" * 200 + "\n")
        print(str(e) + "\n" + "*" * 20 + "\n" + "\nPlease Enter the Credentials Again.")
        infoList = serverReceiver()
        bigIP = bigIPAuthenticator(infoList)
    return bigIP

def fullPoolInfo(rawPool):
    for key in rawPool:
        print(key.upper() + "\n" + str(rawPool[key]) + "\n")

def fullNodeInfo(rawNode):
        for key in rawNode:
            print(key.upper() + "\n" + str(rawNode[key]) + "\n")

def poolLister(bigIP):
    pools = bigIP.tm.ltm.pools.get_collection()
    for pool in pools:
        print(pool.name + "\n" + "BASIC POOL INFO:\n")
        fullPoolInfo(pool.raw)
        print("*" * 200)


def nodeLister(bigIP):
    nodes = bigIP.tm.ltm.nodes.get_collection()
    for node in nodes:
        print(node.name)
        fullNodeInfo(node.raw)
        print("*" * 200)

def viewOptions():
    userChoice = input("Type 'n' for node info or 'p' for pool info or 'q' to quit: ")
    if userChoice == "n":
        nodeLister(bigIP)
        viewOptions()
    elif userChoice == "p":
        poolLister(bigIP)
        viewOptions()

#TODO: Print out all the pools, nodes, and VIP names alongside their IPs



#main section
infoList = serverReceiver()
bigIP = bigIPAuthenticator(infoList)
viewOptions()
