import tkinter as tk
from tkinter import filedialog
import random
import pyaudio
import wave

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.frame = tk.Frame(self,bg="black")
        self.frame.pack(side="top", fill=tk.X)

        self.display = tk.Text(self.frame, height=1)
        self.display['fg']="blue"
        self.display.pack(padx=5, pady=10, side="left")

        self.datas = []
        self.filename = ""
        self.recorded = False
        
        # self.display = tk.Text(self, height=1)
        # self.display['fg']="blue"
        # self.display.pack(side="bottom", padx=5, pady=10, fill=tk.X)
        # self.display.insert(tk.END, "Useful display Here !")
        
        self.create_widgets()

    def create_widgets(self):
        self.display.insert(tk.END, "Select a File")

        self.generate = tk.Button(self.frame, bg="black", fg="white", command=self.sentenceDisplay)
        self.generate["text"] = "Generate"
        self.generate.pack(padx=5, pady=10, side="right")

        self.select = tk.Button(self, bg="black", fg="white", command=self.openFile)
        self.select["text"] = "Select a File"
        self.select.pack(padx=5, pady=10, fill=tk.X)

        self.recorderFrame = tk.Frame(self)
        self.recorderFrame.pack(side="bottom", fill=tk.X)

        self.record = tk.Button(self.recorderFrame, bg="black", fg="white", command=self.recordAudio)
        self.record["text"] = "Record"
        self.record.pack(padx=5, pady=10, fill=tk.X)

        self.record = tk.Button(self.recorderFrame, bg="black", fg="white", command=self.play)
        self.record["text"] = "Play"
        self.record.pack(padx=5, pady=10, fill=tk.X)

    def play(self):
        if not self.recorded:
            self.display.delete(1.0, tk.END)
            self.display.insert(tk.END, "Please record first")
            return

        chunk = 1024  

        wf = wave.open("datasets/"+self.filename+".wav", 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                        channels = wf.getnchannels(),
                        rate = wf.getframerate(),
                        output = True)

        data = wf.readframes(chunk)

        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        wf.close()
        stream.close()
        p.terminate()

    def recordAudio(self):
        if not self.filename:
            self.display.delete(1.0, tk.END)
            self.display.insert(tk.END, "Please select a file first")
            return

        chunk = 1024  
        sample_format = pyaudio.paInt16
        channels = 2
        fs = 44100  
        seconds = 10

        p = pyaudio.PyAudio()  

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  

        
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        
        stream.stop_stream()
        stream.close()
        
        p.terminate()

        wf = wave.open("datasets/"+self.filename+".wav", 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        self.recorded = True

    def openFile(self):
        self.select = filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        if self.select:
            with open(self.select, 'r') as f:
                for row in f:
                    self.datas.append(row)
        else:
            self.display.delete(1.0, tk.END)
            self.display.insert(tk.END, "Please, Select a File")


    def sentenceDisplay(self):
        self.display.delete(1.0, tk.END)
        try:
            self.filename = random.choice(self.datas)
            self.display.insert(tk.END, self.filename)
        except IndexError:
            self.display.delete(1.0, tk.END)
            self.display.insert(tk.END, "Please, Select a File")


root = tk.Tk()
root["bg"] = "black"
root.title("Hello, World")
app = Application(master=root)
app.mainloop()