class Student:
    def __init__(self, n, a, m):
        self.name = n
        self.age = a
        self.marks = m
        
    def display(self):
        print("Hi", self.name)
        print("Your age", self.age)
        print("Your marks", self.marks)
        
    s1 = Student("Dakalo", 26, science = 95, english = 90, maths = 90) 
    s1.display()
    print("----")
    s2 = Student("Mpho", 25, science = 90, english = 95, maths = 92) 
    s2.display()
        
    