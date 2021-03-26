from User import *

def start():     #db test
    newUser = input('Welcome to David\'s Weight Tracking Python Project. \nAre you a returning or new user? (R/N)\n')
    if newUser == 'N' or newUser == 'New':
        createUser() 
    else:
        returnUser()
        #working on graph

start()