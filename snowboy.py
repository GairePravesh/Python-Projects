import snowboydecoder
import sys
import signal
import pyttsx
engine=pyttsx.Engine()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[9].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-10)
# Demo code for listening two hotwords at the same time
def trigger():
    speak("Claps for the crowd")
	
def lightCmd():
    speak("Lights on off for the room")

def musicCmd():
    speak("Random Music Play for my mood")

def movieCmd():
    speak("Play movie to watch")

def stopCmd():
    speak("Stop played things its annoying")

def curtainCmd():
    speak("Curtains up down accordingly")

def exitCmd():
    speak("Good bye see u soon")
    detector.terminate()
    listenTrig()

def test():
    print "Works"

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def speak(text):
    engine.say(text)
    engine.runAndWait()
interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


models = ["models/claps.pmdl","models/lights.pmdl","models/Music.pmdl","models/Stop.pmdl","models/Movie.pmdl","models/curtains.pmdl","models/Exit.pmdl"]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.55]*7
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: trigger(),lambda: lightCmd(), lambda: musicCmd(), lambda: stopCmd(), lambda: movieCmd(), lambda: curtainCmd(), lambda: exitCmd()]
print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
