class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def introduce(self):
        print(f"Hi, I am {self.name} age {self.age} grade {self.grade}")
        
    
student1 = Student("Likitha", 25, "A")
student2 = Student("Rahul", 23, "B")
student1.introduce()
student2.introduce()
print(student1.name)
print(student2.name)