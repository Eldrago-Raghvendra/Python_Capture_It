class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
     
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

a = int(input("Enter the first no.:"))
b = int(input("Enter the second no.:"))
obj = calc(a,b)

def operation():
    x=(" 1. Add \n 2. Sub\n 3. Mult\n 4. Div")
    print(x)
operation()

option = int(input("Chosse one of the Operations:"))
if option==1:
    print("Ans:", obj.add())
elif option==2:
    print("Ans:", obj.sub())       
elif option==3:
    print("Ans:", obj.mult())  
elif option==4:
    print("Ans:", obj.div())
else:
    print("Invalid choice")
