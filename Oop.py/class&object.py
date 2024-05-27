#Class A Car 

#driving()

#Methods refuel() getFuel setSpeed() drive()

#attributes fuel maxspeed

#Our first class

class Student: 
    def _init_(self):
        self.name = 'Dakalo'
        self.age = 20
        self.marks = 95
        
def talk(self):
    print("Name -", self.name)
    print("Age -", self.age)
    print("Marks -", self.marks)
    
s1 = Student()
s1.name = "Sadiki"
print(s1.name)



#init is to initialize the variable it automatically call a class 

class Student: 
    def _init_(self):
        self.name = 'Dakalo'
        self.age = 20
        self.marks = 95
       
        
def talk(self):
    print("Name -", self.name)
    print("Age -", self.age)
    print("Marks -", self.marks) 
    
  #constractor they call themself  
s1 = Student()
print(id(s1))

s2 = Student()
print(id(s2))