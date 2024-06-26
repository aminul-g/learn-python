''' 
Create a class “Programmer” for storing information of few programmers 
working at Microsoft.
'''
class Programmer:
      def __init__(self,name, language, salary):
            self. name = name
            self.language = language
            self.salary = salary
      def display(self):
            print(f"Name: {self.name}\nLanguage:{self.language}\nSalary: {self.salary}\n")
ob1 = Programmer("Aminul","Python",12000)
ob1.display()
ob2 = Programmer("Amin","C++",15000)
ob2.display()
ob3 = Programmer("Hadi","c",20000)
ob3.display()