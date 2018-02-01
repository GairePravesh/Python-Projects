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

def test():
    print "Works"

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def listenTrig():
    #trigModel=sys.argv[1:1] 
    trigModel="models/claps.pmdl"
    print("System at rest. Trigger it to use system")
    detector = snowboydecoder.HotwordDetector(trigModel, sensitivity=0.4,audio_gain=1)
    #detector.start(detected_callback=listenCmd(), interrupt_check=interrupt_callback,sleep_time=0.03)
    detector.start(detected_callback=test(), interrupt_check=interrupt_callback,sleep_time=0.03)

#claps 0.4
#lights 0.55
#music 0.5
#stop 0.4
#movie 0.55
#curtains 0.5
#exit 0.5

def listenCmd(): 
    print('What do you want me to do sir')
    #cmdModels = sys.argv[2:]
    #val=[0.55,0.5,0.4,0.55,0.5,0.5]
    val=[0.5]*6
    cmdModels=["models/lights.pmdl","models/Music.pmdl","models/Stop.pmdl","models/Movie.pmdl","models/curtains.pmdl","models/Exit.pmdl"]
    detector = snowboydecoder.HotwordDetector(cmdModels, sensitivity=val,audio_gain=1)
    callbacks = [lambda: lightCmd(), lambda: musicCmd(), lambda: stopCmd(), lambda: movieCmd(), lambda: curtainCmd(), lambda: exitCmd()]
    detector.start(detected_callback=callbacks, interrupt_check=interrupt_callback, sleep_time=0.03)

import snowboydecoder
#import sys
import signal
interrupted = False 
'''   
if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python program_file_name model_name")
    sys.exit(-1)
'''
signal.signal(signal.SIGINT, signal_handler)
listenTrig()
