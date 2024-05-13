# # class Student:
# #     college_name = "PPS"#it is a class attributes,and class attri is shared to all instances of the class
    
# #     def __init__(self, name , marks) :#>iniit method used for initializing newly created objects
# #          self.name = name#name & marks are instance attributes
# #          self.marks = marks

# #          # print("checking bro"
# #     def welcome(self):#>>self refers to instance itself
# #        print("welcome students,",self.name)


# # s1 = Student("karan",89)


# # s1.welcome()

# # print(s1.name,s1.marks,s1.college_name)


# # #class attributes and object attributes
# # s2 = Student("arjun",93)
# # print(s2.name,s2.marks,Student.college_name)#obj attribute>>class attribute 

 
# # class car:
# #     color="yellow"
# #     brand="mercedes"


# # # mycar=car()
# # # print(mycar.color)
# # # print(mycar.brand)  


# # # Q-1>> create Student classs that takes names & marks of three sujectsas arguments inn constructor.then create a method to printt the average

# class Student:

#     def __init__(self, name , marks):
#          self.__name = name
#          self.marks = marks

        
        
#          def result():
#           print(self.__name)
       
# # #     def get_avg(self):
# # #         sum=0
# # #         for val in self.marks:
# # #                 sum+=val

# # #         print("hi",self.name,"your avg marks are",sum/3)
         
# s1 = Student("mudasir", [99,98,97])
# print(s1.marks)


# # s1.get_avg()


# # banking system

# # create account classs witth two attributes balnce& account no,create method forr debit,credit aand printing the balance

# class Account:
#     def __init__(self,bal,acc):#>>init method used for initializing newly created objects
#         self.balance = bal
#         self.__account_no = acc 
 
#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs",amount,"has debited")
#         print("total balance=",self.get_balance())

#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs",amount,"has credited")
#         print("total balance=",self.get_balance())


#     def get_balance(self):
#         return self.balance            


# acc1=Account(20000,436)
# acc1.debit(6000)
# acc1.credit(4000)
# acc1.debit(2000)

# class  Teacher: 
#     t_name = 'sir hamad',
#     t_id = 13102,
# T1 = Teacher()
# del T1
# print(T1.t_id)
# T2 = Teacher()
# print(T2.t_name)

# >> public and private

# class person:     
#  __name="noone"


#  def __hello(self):
#      print("hello boy")

#  def welcome(self):
#      self.__hello() 

# p1=person()

# print(p1.welcome())
  
class Car:
     def __init__(self,type): 
       self.type=type

@staticmethod
def start():
    print("car started")

@staticmethod      
def stop():
 print("car stopped")

class toyota_car(Car): 
  def __init__(self,name,type  ): 
    self.name = name
    super().__init__(type)

car1 =toyota_car("2D","electric")  
print(car1.type)
car1.name
   

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

    
#   def printname(self):
#     print(self.firstname, self.lastname)

# #   def printname(self):
# #     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
# #     Person.__init__(self, fname, lname)

#    self.firstname = fname
#    self.lastname = lname
#    print(self.firstname, self.lastname)

# x = Student("Mike", "Olsen")
# x.printname()






        
