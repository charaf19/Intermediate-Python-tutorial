class Person: 
    #constructor==== la methode qui permet de creer un nouveau objet et c'est juste uen redefinition de cette methode
    def __init__ (self,name,age,height):
        #give to the object some attributs 
        self.name='charaf'
        self.age = 12
        print('Hello!world!!')
        #auto  increment the amount of the objects that we have created  
        self.amount+=amount
    #method that calculate age of the object created
    def get_older(years):
        self.age+=years 
    
    def __str__(self):
        return f"Name{self.name}, the height{self.height}, the age{self.age}"

#define a class that inherit from the class person
class Worker(Person):
    def __init__ (self,name,age,height,salary):
        
        super(Worker,self).__init__(self,name,age,height,salary)
            self.name=name
            self.age = age
            self.height = height
            self.salary=salary

        #define a method of the child class 
        def calc_salary(self):
            return self.salary * 12
        
        def __str__(self):
            #means that i am working the attributs of the worker and not the one for the person 
            text=super(Worker,self).__str__(self)
            text+=f"salary{self.salary}"
            return text

worker1=Worker('charaf',23,176,35000)
print(worker1.calc_salary())
