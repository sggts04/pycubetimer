import time
from tkinter import *
import keyboard
from pyTwistyScrambler import scrambler333

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
    global b, timed, count, times_list, p, avg5, avg5_flo, times_list_5_flo, times_list_5, min_5, max_5, min_c, max_c
    b=b+1
    scramble.config(text = scrambler333.get_WCA_scramble())
    times_file = open('times.txt', 'a+')
    times_file.write(timed + '\n')
    times_file.close()
    times_file = open('times.txt', 'r')
    times_list = times_file.readlines()
    count = len(times_list)
    times_file.close()
    i = 1
    saved_times_str = ''
    if (count < 12):
        while (i <= count):
            if (i == count):
                saved_times_str = saved_times_str + times_list[count - i].strip()
                break
            saved_times_str = saved_times_str + times_list[count - i].strip() + ', '
            i = i + 1
    else:
        while (i < 13):
            if (i == 12):
                saved_times_str = saved_times_str + times_list[count - i].strip()
                break
            saved_times_str = saved_times_str + times_list[count - i].strip() + ', '
            i = i + 1
    times_count.config(text='No. of Solves: ' + str(count))
    saved_times.config(text='Last 12 Solves: ' + saved_times_str)
    avg5 = ''
    avg5_flo = 0
    min_c = 0
    max_c = 0
    if (count > 5):
        times_list_5 = times_list[count - 5:count]
        times_list_5_flo = [0, 1, 2, 3, 4]
        p = 0
        while (p < 5):
            times_list_5_flo[p] = float(times_list_5[p].strip())
            p = p + 1
        min_5 = min(times_list_5_flo)
        max_5 = max(times_list_5_flo)
        p = 0
        while (p < 5):
            if (times_list_5_flo[p] == max_5 and max_c == 0):
                p = p + 1
                max_c = 1
                continue
            if (times_list_5_flo[p] == min_5 and min_c == 0):
                p = p + 1
                min_c = 1
                continue
            avg5_flo = avg5_flo + (times_list_5_flo[p] / 3)
            p = p + 1
        avg5 = '%.2f' % (avg5_flo)
    ao5.config(text = 'Average of 5: ' + avg5)
    root.update()

root = Tk()
root.config(background='#f6e58d')
times_file = open('times.txt', 'r')
times_list = times_file.readlines()
count = len(times_list)
times_file.close()
timer = Label(root, text = '0.00', font=('Helvetica', 100), background='#f6e58d', fg = 'black')
img1 = PhotoImage(file="start.png")
img2 = PhotoImage(file="stop.png")
start = Button(root, text = ' Start', height = 50, background = 'white', width= 120, command = watch, image=img1, compound = LEFT, font=('Verdana', 20))
stop = Button(root, text = ' Stop', height = 50, background = 'white', width= 120, command = freeze, image=img2, compound = LEFT, font=('Verdana',20))
times_count = Label(root, text = 'No. of Solves: ' + str(count), font=20, background='#f6e58d', fg = 'black')
i=1
saved_times_str = ''
if(count<12):
    while (i <= count):
        if (i == count):
            saved_times_str = saved_times_str + times_list[count - i].strip()
            break
        saved_times_str = saved_times_str + times_list[count - i].strip() + ', '
        i = i + 1
else:
    while(i<13):
        if(i==12):
             saved_times_str = saved_times_str + times_list[count - i].strip()
             break
        saved_times_str = saved_times_str + times_list[count-i].strip() + ', '
        i = i+1

saved_times = Label(root, text = 'Last 12 Solves: ' + saved_times_str, font=20, background='#f6e58d', fg = 'black')
scramble = Label(root, text = scrambler333.get_WCA_scramble(), font=20, background = '#f6e58d', fg='black')
timer.grid(row=1, columnspan=2, padx = 20, pady = 20)
start.grid(row=2, pady=15, padx=10)
stop.grid(row=2, column=1, pady=15, padx=10)
times_count.grid(row=3, columnspan=2, pady =10, padx = 5)
saved_times.grid(row=4, columnspan=2, pady=10, padx = 10)
scramble.grid(row=0, columnspan=2, pady=15, padx = 5)
avg5 = ''
avg5_flo = 0
max_c=0
min_c=0
if(count>=5):
    times_list_5 = times_list[count-5:count]
    times_list_5_flo = [0,1,2,3,4]
    p=0
    while(p<5):
        times_list_5_flo[p] = float(times_list_5[p].strip())
        p=p+1
    min_5 = min(times_list_5_flo)
    max_5 = max(times_list_5_flo)
    p=0
    while(p<5):
      if(times_list_5_flo[p] == max_5 and max_c == 0):
         p=p+1
         max_c = 1
         continue
      if(times_list_5_flo[p] == min_5 and min_c == 0):
          p = p + 1
          min_c = 1
          continue
      avg5_flo = avg5_flo + (times_list_5_flo[p]/3)
      p = p+1
    avg5 = '%.2f' % (avg5_flo)
ao5 = Label(root, text = 'Average of 5: ' + avg5, font=20, background='#f6e58d', fg = 'black')
ao5.grid(row=5, columnspan = 2, pady=5, padx=10)
root.title('Cube Timer')
root.mainloop()
