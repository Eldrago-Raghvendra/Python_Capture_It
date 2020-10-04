my_string=input("Enter the string:")
str=""
for i in my_string:
    str=i+str
print("Reversed string:",str)

####


    
####
p=input("Enter first string:")
q=input("Enter second string:") 

if q in p:
    print("Its a part of first string")
else:
    print("It is not a part of first string")
