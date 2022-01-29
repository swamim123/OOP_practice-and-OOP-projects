from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user= input()
        if input_of_user== stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylog.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")

if __name__ == '__main__':

    # musiconloop("doremon.mp3","stop")
    init_water  =time()
    init_eyes = time()
    init_excercise = time()
    watersecs=40*60
    eyesecs=30*60
    excersecs=45*60

    while True:
        if time() -init_water>watersecs:
            print("Water drinking time.Enter 'drank' to stop the alarm")
            musiconloop("doremon.mp3","drank")
            init_water=time()
            log_now("drank water at")

        if time() - init_eyes > eyesecs:
            print("Eye excercise time.Enter 'done' to stop the alarm")
            musiconloop("doremon.mp3", "done")
            init_eyes = time()
            log_now("Eyes excercuse done at")

        if time() - init_excercise > excersecs:
            print("Excersize time.Enter 'done'to stop the alarm")
            musiconloop("alert_tone.mp3", "done")
            init_excercise = time()
            log_now("Excersize done at")