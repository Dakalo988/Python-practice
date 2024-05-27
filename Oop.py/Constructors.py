#It is possible to define Multiple Constructors in Python?

class Student: 
    def __init__(self, n):
        self.name = n
    
    def display(self):
        print("Hi", self.name)
        
    def display(self):
        print("Hi",)
        
    s1 = Student("Shubham") 
    s1.display()
    
    