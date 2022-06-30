import sqlite3
#connecting to database if exisits or create it if it doesn't
connection = sqlite3.connect('mydata.db')
#the cursor is the interface that allows us to connect with the database
cursor = connection.cursor()
#create a class to create objects and load these object to the database
class Person:
    def __init__(self ,nu=-1,first="",last="",age=-1):
        self.id_number = nu
        self.first = first
        self.last = last
        self.age = age
        #connecting into the database
        self.connection = sqlite3.connect('mydata.db')
        self.cursor=self.connection.cursor()


    def load_person(self,id_number):
        cursor.execute('SELECT * FROM PERSONS WHERE ID={}'.format(id_number))
        results = cursor.fetchone()
        self.id_number=id_number
        self.first=results[1]
        self.last=results[2]
        self.age=results[3]
    def insert_person


#the method exxecute is where we will place our queries
#create a new table with 3 columns
cursor.execute("""
CREATE TABLE IF NOT EXISTS PERSONS(
    ID INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

#insert data to the table in the database
cursor.execute("""
INSERT INTO PERSONS VALUES
(1,'amine','amine',22),(2,'salim','amine',43),(3,'hamid','amine',55)
""")
#create a new person using the class persons

p1= Person()
p1.load_person(1)


#TO EXTRACTTHE RECORDS ON THE TABLE WE EXECUTE THE SELECT STATEMENT
cursor.execute("""
SELECT * FROM PERSONS 
""")

#to iterate in the records in the cursor
rows = cursor.fetchall()
print(rows)

#to show the first name of the object person

print(p1.first)

#to apply the changes to the database
connection.commit()
#every time we have to close the connection
connection.close()
