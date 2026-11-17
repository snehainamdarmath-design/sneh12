class employee:
     def __init__(self,name,salary,department):
          self.name = name
          self.salary = salary
          self.department =department
     def display(self):
               print("name:",self.name)
               print("salary",self.salary)
               print("department",self.department)

s1=employee("mahima",900000,"sales")
s2=employee("mahii",10000,"finance")

s1.display()
s2.display()
