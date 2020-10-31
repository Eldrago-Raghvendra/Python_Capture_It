a = {}
n = int(input("enter a value:"))
for i in range(n):
    keys = input() 
    values = int(input())
    if(len(keys)<=6 and values%2==0):
        a[keys] = values
print(a)
