# CREATE THE CLASS
class ATM(object):
    #CREATE __INIT__ FUNCTION 
    #IT IS SAME LIKE CONSTRUCTO IN JAVA
    def __init__(self,name,age,cardNumber,PIN,TotalAmount):
        #USE SELF 
        #IT IS SAME LIKE THIS IN JAVA
        self.name = name
        self.age = age
        self.cardNumber = cardNumber
        self.PIN = PIN
        self.TotalAmount = TotalAmount

#CREATE SOME FUNCTIONS
    def EnterCardNumber(self):
        print("ENTER CARD NUMBER")

    def EnterPIN(self):
        print("ENTER PIN")

    def TotalBalance(self):
        print("RS. 500000")

    def Withdraw(self):
        print("AMOUNT WITHDRAW SUCCESSFUL")

    def Add(self):
        print("AMOUNT ADDED SUCESSFULLY")


#CREATE SOME OBJECTS AND CALL THE CLASS FUNCTIONS 
#SHOW THE FUNCTIONS USING PRINT
person1 = ATM("RAHUL ARORA",34,"1576XXXXXX98","2*****9","$80,000")
print(person1.EnterCardNumber())
print(person1.EnterPIN())
print(person1.TotalBalance())
print(person1.Withdraw())
print(person1.Add())

person2 = ATM("GEORGE SUTHERLAND",22,"2400XXXXXX89","6********2","$44,000")
print(person2.EnterCardNumber())
print(person2.EnterPIN())
print(person2.TotalBalance())
print(person2.Withdraw())
print(person2.Add())