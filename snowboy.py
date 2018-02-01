def trigger():
    print("Claps")
	
def lightCmd():
    print("Lights")

def musicCmd():
    print("Random Music Play")

def movieCmd():
    print("Play movie")

def stopCmd():
    print("Stop played things")

def curtainCmd():
    print("Curtains")

def exitCmd():
    print("Good bye")
    detector.terminate()
    listenTrig()

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def listenTrig():
    trigModel=sys.argv[1:1] 
    #trigModel="models/clap.pmdl"
    print("System at rest. Trigger it to use system")
    detector = snowboydecoder.HotwordDetector(trigModel, sensitivity=0.35)
    detector.start(detected_callback=listenCmd(), interrupt_check=interrupt_callback,sleep_time=0.03)

def listenCmd(): 
    print('What do you want me to do sir')
    cmdModels = sys.argv[2:]
    #cmdModels=["lights.pmdl","music.pmdl","stop.pmdl","movie.pmdl","curtain.pmdl","exit.pmdl"] 
    detector = snowboydecoder.HotwordDetector(cmdModels, sensitivity=0.35)
    callbacks = [lambda: lightCmd(), lambda: musicCmd(), lambda: stopCmd(), lambda: movieCmd(), lambda: curtainCmd(), lambda: exitCmd()]
    detector.start(detected_callback=callbacks, interrupt_check=interrupt_callback, sleep_time=2)

import snowboydecoder
import sys
import signal
interrupted = False    
if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python program_file_name model_name")
    sys.exit(-1)
signal.signal(signal.SIGINT, signal_handler)
listenTrig()
