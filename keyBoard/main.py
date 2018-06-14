from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
import random
from threading import Timer
import pyautogui as gui
import timeit

class KeyBoard(Frame):
    old,now=0,0
    oldx,oldy=0,0
    newx,newy=0,0
    
    def __init__(self,parent):
        super().__init__()
        self.root=parent
        self.initUI()
        
                
    def initUI(self):
        self.master.title("Keyboard")
        self.master.resizable(False,False)
        width = self.master.winfo_screenwidth()
        height= self.master.winfo_screenheight() 
        #x=self.master.winfo_screenwidth()-width
        #y=self.master.winfo_screenheight()-height
        self.master.geometry('%dx%d+%d+%d'%(width//2,height,width//2,0))
        self.predictDisplay(["hello ","world","dfg"])
        self.alphabets()
        self.num_sym()
        self.pack()
        
     
    def predictDisplay(self,words):
        topBar=tk.Frame(self,bd=2 ) 
        tk.Label(topBar,text="Predicted Words",height=2).pack()   
        n=0
        for word in words:
            n+=1
            if n>5:
                break
            btn=tk.Button(topBar,text=word,height=2,width=5,command= lambda k=word:self.attach_key_to(k))
            btn.bind("<Enter>",self.hoverTime)
            btn.bind("<Leave>",self.cancelTimer)
            btn.pack(side=LEFT,padx=5,pady=5)
            topBar.pack()
     
    def alphabets(self):
        n,c,r=0,0,1
        letters=list("qwertyuiopasdfghjklzxcvbnm") 
        alphaBar=tk.Frame(self,bd=2)
        tk.Label(alphaBar,text="Alphabets",height=2).grid(row=0,column=0,sticky='nwes',columnspan=10)
        for letter in letters:
            btn=tk.Button(alphaBar,text=letter,height=2,width=5,command=lambda k=letter:self.attach_key_to(k))
            btn.bind("<Enter>",self.hoverTime)
            btn.bind("<Leave>",self.cancelTimer)
            btn.grid(row=r,column=c,pady=3)
            alphaBar.pack()
            n+=1
            c+=1
            if n==10:
                r+=1
                c=0
            elif n==19:
                r+=1
                c=0
        btn=tk.Button(alphaBar,text='Space',height=3,command=lambda : self.attach_key_to('Space'))
        btn.bind("<Enter>",self.hoverTime)
        btn.bind("<Leave>",self.cancelTimer)
        btn.grid(row=5,column=0,sticky='nwes',columnspan=10)
        tk.Label(alphaBar,height=1).grid(row=4,column=0,sticky='nwes',columnspan=10)
        btn=tk.Button(alphaBar,text='Back',height=3,command=lambda : self.attach_key_to('Back'))
        btn.bind("<Enter>",self.hoverTime)
        btn.bind("<Leave>",self.cancelTimer)
        btn.grid(row=6,column=0,sticky='nwes',columnspan=3)
        btn=tk.Button(alphaBar,text='Enter',height=3,command=lambda : self.attach_key_to('Enter'))
        btn.bind("<Enter>",self.hoverTime)
        btn.bind("<Leave>",self.cancelTimer)
        btn.grid(row=6,column=3,sticky='nwes',columnspan=3)
        btn=tk.Button(alphaBar,text='Mouse',height=5,command=lambda : self.attach_key_to('Mouse'))
        btn.bind("<Enter>",self.hoverTime)
        btn.bind("<Leave>",self.cancelTimer)
        btn.grid(row=6,column=6,sticky='nwes',columnspan=4)
        alphaBar.pack()
              
    def num_sym(self):
        n,c,r=0,0,1
        nums=list("1234567890") 
        syms=list("-+=*/.,\\<>?;:'%$^&#@")
        numBar=tk.Frame(self,bd=2)
        tk.Label(numBar,text="Numbers & Symbols",height=2).grid(row=0,column=0,sticky='nwes',columnspan=10)
        for num in nums:
            btn=tk.Button(numBar,text=num,height=2,width=5,command=lambda k=num:self.attach_key_to(k))
            btn.bind("<Enter>",self.hoverTime)
            btn.bind("<Leave>",self.cancelTimer)
            btn.grid(row=r,column=c,pady=3)
            numBar.pack()
            n+=1
            c+=1
            if n==10:
                r+=1
                c=0
            elif n==19:
                r+=1
                c=0
        n,c,r=0,0,1
        symBar=tk.Frame(self,bd=2)
        for sym in syms:
            btn=tk.Button(symBar,text=sym,height=2,width=5,command=lambda k=sym:self.attach_key_to(k))
            btn.bind("<Enter>",self.hoverTime)
            btn.bind("<Leave>",self.cancelTimer)
            btn.grid(row=r,column=c,pady=3)
            symBar.pack()
            n+=1
            c+=1
            if n==10:
                r+=1
                c=0
            elif n==20:
                r+=1
                c=0
        
    def attach_key_to(self,k):
        print(k)
        #/* work place for you */
        if k=="Mouse":
            self.cancelTimer()
            #self.grid_forget()
            #self.pack_forget()             
            self.root.withdraw()
            #self.root.deiconify()
            self.mouse()    
   
    def hoverTime(self,event=None):
        self.old = timeit.default_timer() 
        self.oldx,self.oldy=gui.position()
        global t
        t=Timer(3,self.checkHover)     
        t.start()

    def cancelTimer(self,event=None):
        global t        
        t.cancel()
        #print("Cancel")

    def checkHover(self,event=None):
        self.new = timeit.default_timer() 
        if int(self.new-self.old)>2: 
            self.newx,self.newy=gui.position()
            gui.click(self.oldx,self.oldy)
            gui.moveTo(self.newx,self.newy)
            #self.hoverTime()
            #print(self.old," and ",self.new)
        else:
           pass 
            
    def mouse(self):
        self.cancelTimer()
        #self.old=0
        #print("momuse")
        m=Tk()
        m.title("Mouse")
        m.resizable(False,False)
        width = m.winfo_screenwidth()//10
        height= m.winfo_screenheight() //10
        x=m.winfo_screenwidth()-width
        y=m.winfo_screenheight()-height
        m.geometry('%dx%d+%d+%d'%(width,height,x,y))  
        btn=tk.Button(m,text="KeyBoard",height=3,width=12,command=lambda : self.multiFunc(m))
        btn.grid(padx=5,pady=5)
        btn.bind("<Enter>",self.hoverTime)
        btn.bind("<Leave>",self.cancelTimer)
        m.protocol("WM_DELETE_WINDOW",lambda:self.close_windows(m))
        m.mainloop()
    
    def close_windows(self,m):
        self.root.destroy()      
        m.destroy()  
    
    def multiFunc(self,m):
        self.root.deiconify()
        m.destroy()
       
def main():
    root = tk.Tk()
    sk=KeyBoard(root)
    root.mainloop()
    #t = None

if __name__=='__main__':
    main()

