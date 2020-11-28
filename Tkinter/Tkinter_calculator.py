import tkinter as tk 
from functools import partial
#================================
def add(label,n1,n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label.config(text="Result is %d"%result)
    return

def sub(label,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    res=int(num1)-int(num2)
    label.config(text="Result is %d"%res)

def mul(label,n1,n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)*int(num2)
    label.config(text="Result is %d"%result)
    
def div(label,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)/int(num2)
    label.config(text="Result is %d"%result)




root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()

labelTitle = tk.Label(root, text=" Calculator").grid(row=0, column=2)
#===============================================
labelNum1 = tk.Label(root, text="Enter a number").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Enter another number").grid(row=2, column=0)
#===============================================
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
add= partial(add,labelResult,number1,number2)
mul= partial(mul,labelResult,number1,number2)
sub= partial(sub,labelResult,number1,number2)
div=partial(div,labelResult,number1,number2)

#==============================================
button=tk.Button(root, text="Add", command=add).grid(row=3, column=1)
button=tk.Button(root, text="Multiply", command=mul).grid(row=3, column=2)
button=tk.Button(root,text="Subtract",command=sub).grid(row=3,column=3)
button=tk.Button(root,text="Divide",command=div).grid(row=4,column=1)

root.mainloop()
