from datetime import date, datetime
import sqlite3
import matplotlib.pyplot as graph

class User:
    def __init__(self, name, initalWeight=0, initalDate=0, goalWeight=0, goalDate=0, Weight=0, Date=0):
        self.name = name
        self.initalWeight = initalWeight 
        self.initalDate = initalDate
        self.goalWeight = goalWeight
        self.goalDate = goalDate
        self.Weight = Weight
        self.Date = Date
        self.dateList = []
        self.weightList = []
    
    def createTable(self):
        db = sqlite3.connect("weighttrack.db") 
        cursor = db.cursor()
        cursor.execute(f"Create TABLE {self.name} (initalWeight REAL,initalDate BLOB, goalWeight REAL, goalDate BLOB, weight REAL, date REAL UNIQUE)")
        cursor.execute(f'INSERT INTO {self.name} VALUES(?, ?, ?, ?, ?, ?)',
            (self.initalWeight, self.initalDate, self.goalWeight, 
            self.goalDate, self.initalWeight, self.initalDate)
            )
        cursor.execute(f'Select * From {self.name}')
        test = cursor.fetchone()
        print(test) #delete once done
        db.commit()
        db.close()

    def getInitalAverage(self):
        average = abs(7*(self.goalWeight-self.initalWeight)/((self.goalDate-self.initalDate).days))
        return round(average, 2)

    def getIntro(self):
        return f"New user {self.name} created with starting weight of {self.initalWeight}.\nYou have to lose {self.getInitalAverage()} lbs a week.\nPlease login daily to update the tracker"

    def updateTable(self):
        self.Weight = input('What is your weight\n')
        self.Date = input('Enter the date (YYYY-MM-DD FORMAT)\n')
        db = sqlite3.connect("weighttrack.db") 
        cursor = db.cursor()
        cursor.execute(f'INSERT INTO {self.name} VALUES(?, ?, ?, ?, ?, ?)',
            (self.initalWeight, self.initalDate, self.goalWeight, 
            self.goalDate, self.Weight, self.Date)
            )
        cursor.execute('select * from Test') #delete 
        test = cursor.fetchall()
        print(test)
        db.commit()
        db.close()
        print('Your weight has been added.')

    def updateList(self): 
        db = sqlite3.connect("weighttrack.db") 
        cursor = db.cursor()
        cursor.execute(f'select weight, date from {self.name}')
        test = cursor.fetchall()
        print(test) #delete once done
        for x in test:
            self.weightList.append(x[0])
            self.dateList.append(x[1])

    def createGraph(self):
        dateListConverted = [datetime.strptime(singledate, '%Y-%m-%d') for singledate in self.dateList]
        goalList = [self.initalDate, self.goalDate]
        goalListConverted = [datetime.strptime(singledate, '%Y-%m-%d') for singledate in goalList]
        graph.plot(dateListConverted, self.weightList, label='Current Progress')
        graph.plot(goalListConverted, [self.initalWeight, self.goalWeight], label='Weight Lost Goal', linestyle='dashed', color='green')
        graph.legend()
        graph.title('Progress Report')
        graph.ylabel('Weight')
        graph.xlabel('Date')
        graph.show()
    
    def createTable(self):
        container = zip(self.dateList, self.weightList)
        for x in container:
            print(f'Date: {x[0]}    |    Weight: {x[1]}     |')

def openTable(name):
    db = sqlite3.connect("weighttrack.db") 
    cursor = db.cursor()
    cursor.execute(f'Select * From {name} where rowid = 1')
    returningList = cursor.fetchone()
    db.commit()
    db.close()
    return returningList
    

def createUser():
    name = input("What is your name? ")
    initalWeight = int(input('Enter starting weight '))
    goalWeight =  int(input('Enter goal weight '))
    goalDate = input('Enter a goal date (YYYY-MM-DD FORMAT) ')
    createdUser = User(name, initalWeight, date.today(), goalWeight, date.fromisoformat(goalDate))
    createdUser.createTable()
    print(createdUser.getIntro())

def returnUser():
    name = input('Pleae enter your name to open your tracker\n')
    data = openTable(name)
    currentUser = User(name, data[0], data[1], data[2], data[3],data[4], data[5])
    action = input(f'Welcome {currentUser.name}, what would you like to do?\n(1) Add Entry Weight\n(2) Check Graph Progress\n(3) Check Past Weigh Ins\n(4) Update Pervious Weight In\n(5) Close Program\n')
    if action == '1':
        currentUser.updateTable()
    elif action == '2':
        currentUser.updateList()
        currentUser.createGraph()
    elif action == '3':
        currentUser.updateList()
        currentUser.createTable()
    elif action == '4':
        pass
        #allow for update to table via sql
        #take in date, change weight

'''
# cursor.execute(f'Select * From {self.name}')
# test = cursor.fetchone()
# print(test)

'''