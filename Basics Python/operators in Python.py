is_male =False
is_tall =False


    
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are not a male or not tall")
elif not(is_male) and is_tall:
    print ("you are not a male but tall")   
else:
    print("you are not male and not tall ")
    
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else :
        return num3
    
print(max_num(400, 20, 3)) 

a = float(input("enter the first num:"))   
op = input("enter the operator:") 
b = float(input("enter the sec num:"))     

if op =="+":
    print(a+b)
elif op =="-":
    print (a-b)
elif op =="*":
    print(a*b)
else:
    print("invalid operator")    
