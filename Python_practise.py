my_string=input("Enter the string:")
str=""
for i in my_string:
    str=i+str
print("Reversed string:",str)

####

rep_string=input("Enter a string:")
if (len(rep_string)<3):
    print("Not Possible in this case")
else:
    a=len(rep_string)
    str1=rep_string[:2]
    str2=rep_string[3:a]
    print(str1+'h'+str2)
    
####
p=input("Enter first string:")
q=input("Enter second string:") 

if q in p:
    print("Its a part of first string")
else:
    print("It is not a part of first string")
