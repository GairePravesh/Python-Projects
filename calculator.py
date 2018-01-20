''''
Pravesh Gaire

Python3.6 tkinter

A simple calculator made using tkinter in python
'''
from tkinter import* #python GUI library
#-----------------------------------------------------------------
def btnClick(number):
    global operator
    operator=operator+str(number)
    textInput.set(operator)#.set() sets text of GUI entry
def btnClear():
    global operator
    operator=""
    textInput.set("")
def btnEqual():
    global operator
    try:
        final=str(eval(operator))#eval evaluates a passed string and returns result
        textInput.set(final)
        operator=""
    except:
        textInput.set("Syntax Error")
        operator=""
#-----------------------------------------------------------------   
root=Tk()
root.resizable(width=False,height=False)
root.title('Calculator')
operator=""
textInput=StringVar()#holds a string with default ""
#-----------------------------------------------------------------
textDisplay=Entry(root,font=('arial',20,'bold'),
                  textvariable=textInput,bd=50,
                  bg="black",fg="white",justify="right").grid(row=0,columnspan=4)#Entry() makes the display screen 
#-----------------------------------------------------------------   
btn7=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=8,command=lambda:btnClick(7)).grid(row=1,column=0)#Button() creates a button
btn8=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=7,command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=9,command=lambda:btnClick(9)).grid(row=1,column=2)
      
Addition=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text='+',command=lambda:btnClick('+')).grid(row=1,column=3)
#-----------------------------------------------------------------      
btn4=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=4,command=lambda:btnClick(4)).grid(row=2,column=0)
      
btn5=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=5,command=lambda:btnClick(5)).grid(row=2,column=1)
      
btn6=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=6,command=lambda:btnClick(6)).grid(row=2,column=2)
      
Subtraction=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text='-',command=lambda:btnClick('-')).grid(row=2,column=3)
#-----------------------------------------------------------------      
btn1=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=1,command=lambda:btnClick(1)).grid(row=3,column=0)
      
btn2=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=2,command=lambda:btnClick(2)).grid(row=3,column=1)
      
btn3=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=3,command=lambda:btnClick(3)).grid(row=3,column=2)
      
Multiply=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text='*',command=lambda:btnClick('*')).grid(row=3,column=3)
#-----------------------------------------------------------------      
btn0=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text=0,command=lambda:btnClick(0)).grid(row=4,column=0)
      
Clear=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text='C',command=btnClear).grid(row=4,column=1)
      
Equals=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text='=',command=btnEqual).grid(row=4,column=2)
      
Divide=Button(root,bd=10,padx=25,pady=25,fg="white",bg="black",
            font=('arial',20,'bold'),text='/',command=lambda:btnClick('/')).grid(row=4,column=3)
#-----------------------------------------------------------------      
root.mainloop()#loops the program
