class Person: 
    #constructor==== la methode qui permet de creer un nouveau objet et c'est juste uen redefinition de cette methode
    def __init__ (self):
        #give to the object some attributs 
        self.name='charaf'
        self.age = 12
        print('Hello!world!!')
#instanciation=== creer un nouveau objet
x = Person()
person1 = Person()
print(person1.name)