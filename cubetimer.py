import time
import sys
from tkinter import *
import keyboard

b = 0
timed = '0.00'

def watch() :
    global b, timed
    b=0
    timed = '0.00'
    now = time.time()
    while (b==0):
        time.sleep(.05)
        timer.config(text="%.2f" % (time.time() - now))
        timed = "%.2f" % (time.time() - now)
        root.update()
        if keyboard.is_pressed('space'):
            freeze()
def freeze():
    global b, timed
    root.update()
    b=b+1
    times_file = open('times.txt', 'a+')
    times_file.write(timed + '\n')
    times_file.close()

root = Tk()
timer = Label(root, text = '0.00', font=('Times',50))
start = Button(root, text = 'Start', height = 2, width= 15, command = watch)
stop = Button(root, text = 'Stop', height = 2, width= 15, command = freeze)
timer.grid(row=0, columnspan=2, padx = 20, pady = 20)
start.grid(row=1, pady=15, padx=5)
stop.grid(row=1, column=1, pady=15, padx=5)
root.title('Cube Timer')
root.mainloop()