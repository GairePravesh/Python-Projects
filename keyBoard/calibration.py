import sys
import tkinter as tk

class Start:
    def __init__(self, master = tk.Tk()):
        self.master = master
        self.i = 0
        w = 150
        h = 100
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x =( ws - w ) // 2  
        y =( hs - h ) // 2
        self.positions= [(w,h,0,0),(w, h, ws-w, 0),(w, h, ws - w, hs - h),(w, h, 0, hs - h)]
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Start Calibration', font=("Helvetica", 15), width=25, height=10, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
        self.master.mainloop()

    def clear_window(self):
        _list = self.master.winfo_children()
        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())
        for item in _list:
            item.pack_forget()

    def new_window(self):
        if self.i == 4:
            sys.exit()
        self.master.geometry('%dx%d+%d+%d' % self.positions[self.i]) 
        self.clear_window()
        self.label = tk.Label(self.master, text="",font=("Helvetica", 32), width=10,height=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(1) 
        self.i += 1
        
    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 0:
            self.new_window()
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.master.after(1000, self.countdown)    

app = Start()
app.mainloop()

