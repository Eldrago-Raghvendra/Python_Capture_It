d = {}
n = int(input("enter a value:"))
for i in range(n):
    keys = input() 
    values = int(input())
    d[keys] = values
print(d)     
d.popitem()
print(d) # 1st method
d.clear()
print(d) # 2nd method
del d
print(d) # 3rd method it will show error since no d is found in memory
