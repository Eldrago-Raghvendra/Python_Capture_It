rep_string=input("Enter a string:")
if (len(rep_string)<3):
    print("Not Possible in this case")
else:
    a=len(rep_string)
    str1=rep_string[:2]
    str2=rep_string[3:a]
    print(str1+'h'+str2)
