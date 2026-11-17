class student:
     def __init__(self,name,age,course):
          self.name = name
          self.age = age
          self.course =course
          def display(self):
               print("name:",self.name)
               print("age",self.age)
               print("course",self.course)

s1=student("mahima",19,"bca")
s2=student("mahii",22,"bba")

s1.display()
s2.display()
