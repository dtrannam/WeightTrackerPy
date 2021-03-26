#used to get sql data
import sqlite3 
import matplotlib.pyplot as graph
db = sqlite3.connect("weighttrack.db") 
cursor = db.cursor()
# records = [
# (190.0, '2020-12-29', 160.0, '2021-03-30', 180, '2021-1-15'),
# (190.0, '2020-12-29', 160.0, '2021-03-30', 175, '2021-2-15'),
# (190.0, '2020-12-29', 160.0, '2021-03-30', 170, '2021-3-15'),
# (190.0, '2020-12-29', 160.0, '2021-03-30', 160, '2021-4-15')]
# # cursor.execute(f"Create TABLE  Test (initalWeight REAL,initalDate BLOB, goalWeight REAL, goalDate BLOB, weight REAL, date REAL UNIQUE)")
# cursor.executemany(f'INSERT INTO Test VALUES(?, ?, ?, ?, ?, ?)', records)
cursor.execute('select weight, date from Test')
test = cursor.fetchall()
print(test)
db.commit()
db.close

'''
(190.0, '2020-12-29', 160.0, '2021-03-30', 0.0, 0.0)
        cursor.execute(f"Create TABLE {self.name} (initalWeight REAL,initalDate BLOB, goalWeight REAL, goalDate BLOB, weight REAL, date REAL)")
        cursor.execute(f'INSERT INTO {self.name} VALUES(?, ?, ?, ?, ?, ?)',
            (self.initalWeight, self.initalDate, self.goalWeight, 
            self.goalDate, self.Weight, self.Date)

(190.0, '2020-12-29', 160.0, '2021-03-30', 180, '2021-1-15')
(190.0, '2020-12-29', 160.0, '2021-03-30', 175, '2021-2-15')
(190.0, '2020-12-29', 160.0, '2021-03-30', 170, '2021-3-15')
(190.0, '2020-12-29', 160.0, '2021-03-30', 160, '2021-4-15')

[(200.0, '2020-12-30', 160.0, '2021-03-30', 0.0, 0.0), (190.0, '2020-12-29', 160.0, '2021-03-30', 180.0, '2021-1-15'), 
(190.0, '2020-12-29', 160.0, '2021-03-30', 175.0, '2021-2-15'), (190.0, '2020-12-29', 160.0, '2021-03-30', 170.0, '2021-3-15'), 
(190.0, '2020-12-29', 160.0, '2021-03-30', 160.0, '2021-4-15')]

'''