import tkinter as tk
import random
import time
import ast
class App:
    def __init__(self, master):
        self.master = master
        master.title("Number Matching Game")
        self.X = self.master.winfo_screenwidth()
        self.Y =  self.master.winfo_screenheight()
        self.master.geometry("%dx%d"%(self.X, self.Y))
        self.btn = [0]*20
        self.prev = None
        self.pres = None
        self.count = 0
        self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 2
        self.guessed = []
        random.shuffle(self.values)
        self.conversion = {
            'A, 1': 0, 'A, 2': 1, 'A, 3': 2, 'A, 4': 3, 'A, 5': 4,
            'B, 1': 5, 'B, 2': 6, 'B, 3': 7, 'B, 4': 8, 'B, 5': 9,
            'C, 1': 10, 'C, 2': 11, 'C, 3': 12, 'C, 4': 13, 'C, 5': 14,
            'D, 1': 15, 'D, 2': 16, 'D, 3': 17, 'D, 4': 18, 'D, 5': 19
        }
        ##print(self.values)
        self.createGrid()
        self.inputCoordinates()

    def createGrid(self):
        r, c = 1, 1
        frame = tk.Frame(self.master)
        frame.pack(padx=10,pady=10)
        label = tk.Label(frame, text="A ", font=('Sans', 20), justify='center')
        label.grid(row =1 ,column = 0)
        label = tk.Label(frame, text="B ", font=('Sans', 20), justify='center')
        label.grid(row=2, column=0)
        label = tk.Label(frame, text="C ", font=('Sans', 20), justify='center')
        label.grid(row=3, column=0)
        label = tk.Label(frame, text="D ", font=('Sans', 20), justify='center')
        label.grid(row=4, column=0)
        label = tk.Label(frame, text="1 ", font=('Sans', 20), justify='center')
        label.grid(row=0, column=1)
        label = tk.Label(frame, text="2 ", font=('Sans', 20), justify='center')
        label.grid(row=0, column=2)
        label = tk.Label(frame, text="3 ", font=('Sans', 20), justify='center')
        label.grid(row=0, column=3)
        label = tk.Label(frame, text="4 ", font=('Sans', 20), justify='center')
        label.grid(row=0, column=4)
        label = tk.Label(frame, text="5 ", font=('Sans', 20), justify='center')
        label.grid(row=0, column=5)
        for i in range(20):
            self.btn[i] = tk.Button(frame,text = '*', width = 15, height = 5,font=('Sans', 10))
            self.btn[i].grid(row = r, column = c)
            c += 1
            if c == 6:
                r += 1
                c = 1

    def inputCoordinates(self):
        frame = tk.Frame(self.master)
        frame.pack(pady=25)
        label =tk.Label(frame, text = "Input your co-ordinates", font = ('Sans',20) )
        label.pack(side ='top')
        self.entry = tk.Entry(frame, justify = 'center' ,font = ('Sans',20))
        self.entry.focus_set()
        self.entry.bind("<Return>", self.check)
        self.entry.pack(ipady=10)
        tk.Button(frame, text = 'Back',command = self.back, height = 2, width = 15).pack(pady = 10)
        tk.Button(frame, text = 'Exit',command = self.master.destroy, height = 2, width = 15).pack()

    def back(self):
        m = mainWindow(self.master)
        m.clear_window()
        m.options()

    def check(self, event = None):
        #print("Checked in to function")
        if self.entry.get() not in self.conversion:
            #print("Wrong input")
            self.entry.delete(0,'end')
            return

        btnNo = self.conversion[self.entry.get()]   
        #print("Input button is %d"%btnNo)
        self.entry.delete(0,'end')
        self.count += 1
        #print("Count incremented to %d"%self.count)
        if self.count == 3:
            #print("Count is 3")
         #   #print("count 3")
            for keys,vals in self.conversion.items():
                self.btn[vals]['text'] = '*'
            self.count = 1
            self.pres = None
            #print("Dictionary is")
            #print(self.conversion)
        self.prev = self.pres
        self.pres = btnNo
        #print("prev and pres are")
        #print(self.prev,self.pres)
#        if self.count 
        if self.count >1  and self.values[self.prev - 1] == self.values[self.pres - 1]:
            #print(" pres Equal to prev")
            #prev = [i for i in range(len(self.values)) if self.values[i] == self.prev]
            #pres = [i for i in range(len(self.values)) if self.values[i] == self.pres]
           # #print(prev,pres)
            #if pres[0] != pres[1]:
            if self.prev != self.pres: 
                #print("different button clicked with same values")
                self.btn[btnNo]['text'] = self.values[self.pres - 1]
                key = [id for (id, no) in self.conversion.items() if no == self.prev]
                #print(key)
                del self.conversion[''.join(key)]
                key = [id for (id, no) in self.conversion.items() if no == btnNo]
                del self.conversion[''.join(key)]
                #print(key)
                #print("new dictionary is")
                #print(self.conversion)
            else:
                #print("Same button clicked twice")
                if self.btn[btnNo]['text'] == '*':
                    self.btn[btnNo]['text'] = self.values[self.pres - 1]
                    self.count =  0
                else:
                    self.btn[btnNo]['text'] = '*'
                    
        else:
            #print("Different button clicked")
            ##print("new press")
            self.btn[btnNo]['text'] = self.values[self.pres - 1]
        
        ##print(self.count)

        #if self.conversion == {}:
        self.complete()
        # print(self.values)
        # Username = self.entrys.get()

    def complete(self):
        new = tk.Tk()
        new.title("Score")
        self.entrys = tk.Entry(new,justify = 'center', font = ('Sans', 20))
        self.entrys.focus_set()
        self.entrys.pack()
        self.entrys.bind("<Return>",lambda x : self.updateScore(new))

    def updateScore(self, new):
        global Username, start
        t = time.time() - start
        Username[0] = self.entrys.get()
        Username[1] = t
        new.destroy()
        #d = {Username[0]:Username[1]}
        with open("scores") as f:
            d = f.read()
        d = ast.literal_eval(d)
        d[Username[1]] = Username[0]
        with open("scores",'w') as f:
            f.write(str(d))
        # print(d)

        # for line in data:
        #     line  = ast.literal_eval(line)
        #     if line[1] > Username[1]:
        #         data.insert(data.index(line),str(Username))
        #         break
        # else:
        #     data.append(str(Username))



        self.back()



class mainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Number Matching Game")
        self.X = self.master.winfo_screenwidth()
        self.Y =  self.master.winfo_screenheight()
        self.master.geometry("%dx%d+%d+%d"%(400, 280,self.X // 2 - 200, self.Y // 2 - 140))
        self.options()

    def options(self):
        frame = tk.Frame(self.master)
        frame.pack(padx = 20, pady = 20)
        play = tk.Button(frame,text = 'Play Game', command = self.playGame, width =15, height = 2)
        play.pack(pady = 5)
        score = tk.Button(frame, text = 'Score', command = self.score, width =15, height = 2)
        score.pack(pady = 5)
        # score = tk.Button(frame, text = 'About', command = self.about, width =15, height = 2)
        # score.pack(pady = 5)
        score = tk.Button(frame, text = 'Exit', command = self.master.destroy, width =15, height = 2)
        score.pack(pady = 5)

    def score(self):
        with open("scores") as f:
            data = ast.literal_eval(f.read())
            new = {}
        sortedScore = sorted(data.keys())
        for c, i in enumerate(sortedScore):
        #      print(data[i], i)
        # print(data)
            new[i] = data[i]
            if c == 9:
                break
        # print(sortedScore)
        with open("scores",'w') as f:
            f.write(str(new))
        self.clear_window()
        frame = tk.Frame(self.master)
        frame.pack()
        for i, key in enumerate(new):
            label = tk.Label(frame, text = str(new[key]) + "    -   " + str("%.2f"%(key)))
            label.grid(row = i,column = 0)
            # print(val,key)
        tk.Button(frame,text = 'Back',height =2,width=20 ,command = lambda  : [self.clear_window(),self.options()]).grid()


    # def about(self):
    #     pass

    def clear_window(self):
        _list = self.master.winfo_children()
        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())
        for item in _list:
            item.pack_forget()

    def playGame(self):
        global start
        start = time.time()
        self.clear_window()
        game = App(self.master)

start = 0
Username = ['User',0]
root =tk.Tk()
app = mainWindow(root)
root.mainloop()
