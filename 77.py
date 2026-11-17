
class student:
    def __init__(self,name,age):
       self.name = name
       self.age = age
    def display(self):
        print(f'name:{self.name},age:{self.age}')
    def study(self,subject):
            print(f'{self.name} is studying{subject}')
s1=student("mahi",19)
s2=student("mahima",20)
s1.display()
s2.display()