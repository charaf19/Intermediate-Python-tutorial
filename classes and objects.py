class Person: 
    #constructor==== la methode qui permet de creer un nouveau objet et c'est juste uen redefinition de cette methode
    def __init__ (self):
        #give to the object some attributs 
        self.name='charaf'
        self.age = 12
        print('Hello!world!!')
        #auto  increment the amount of the objects that we have created  
        self.amount+=amount
    #method that calculate age of the object created
    def get_older(years):
        self.age+=years
#instanciation=== creer un nouveau objet
x = Person()
person1 = Person()
print(person1.name)
#create an object with parameters
class Student:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
#definig a method 
    def SayHelloWorld(self):
        print('hello world')
#defining destructor 
    def __del__(self):
        print('object deleted ')
#defining the str method 
    def __str__(self):
        return f"Name{self.name}, the height{self.height}, the age{self.age}"

#create objencts from the class student with parameters 
etudiant1=Student('charaf',23,'1,45')
print(etudiant1.name)
print(etudiant1.height)
print(etudiant1.age)