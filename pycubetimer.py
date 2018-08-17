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
    global b, timed, count, times_list, p, avg5, avg5_flo, times_list_5_flo, times_list_5, min_5, max_5, min_c, max_c, avg12, avg12_flo, times_list_12_flo, times_list_12, min_12, max_12, min_c12, max_c12, k ,mean
    b=b+1
    scramble.config(text = scrambler333.get_WCA_scramble())
    times_file = open('times.txt', 'a+')
    times_file.write(timed + '\n')
    times_file.close()
    times_file = open('times.txt', 'r+')
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
    if (count >= 5):
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
    avg12 = ''
    avg12_flo = 0
    max_c12 = 0
    min_c12 = 0
    if (count >= 12):
        times_list_12 = times_list[count - 12:count]
        times_list_12_flo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        p = 0
        while (p < 12):
            times_list_12_flo[p] = float(times_list_12[p].strip())
            p = p + 1
        min_12 = min(times_list_12_flo)
        max_12 = max(times_list_12_flo)
        p = 0
        while (p < 12):
            if (times_list_12_flo[p] == max_12 and max_c12 == 0):
                p = p + 1
                max_c12 = 1
                continue
            if (times_list_12_flo[p] == min_12 and min_c12 == 0):
                p = p + 1
                min_c12 = 1
                continue
            avg12_flo = avg12_flo + (times_list_12_flo[p] / 10)
            p = p + 1
        avg12 = '%.2f' % (avg12_flo)
    ao12.config(text='Average of 12: ' + avg12)
    k = 0
    mean = 0
    while (k < count):
        mean = mean + (float(times_list[k].strip()) / count)
        k = k + 1
    mean = '%.2f' % (mean)
    meantotal.config(text='Total Mean: ' + mean)
    root.update()


root = Tk()
root.config(background='#f6e58d')
times_file = open('times.txt', 'a+')
times_file.close()
times_file = open('times.txt', 'r+')
times_list = times_file.readlines()
count = len(times_list)
times_file.close()
timer = Label(root, text = '0.00', font=('Helvetica', 100), background='#f6e58d', fg = 'black')
img1 = PhotoImage(file="start.png")
img2 = PhotoImage(file="stop.png")
start = Button(root, text = ' Start', height = 70, background = 'white', width= 150, command = watch, image=img1, compound = LEFT, font=('Verdana', 20))
stop = Button(root, text = ' Stop', height = 70, background = 'white', width= 150, command = freeze, image=img2, compound = LEFT, font=('Verdana',20))
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
timer.grid(row=1, columnspan=3, padx = 20, pady = 20)
start.grid(row=2, pady=15, padx=10)
stop.grid(row=2, column=2, pady=15, padx=10)
times_count.grid(row=3, columnspan=3, pady =10, padx = 5)
saved_times.grid(row=4, columnspan=3, pady=10, padx = 10)
scramble.grid(row=0, columnspan=3, pady=15, padx = 5)
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
ao5.grid(row=5, column=0, pady=5, padx=10)
avg12 = ''
avg12_flo = 0
max_c12=0
min_c12=0
if(count>=12):
    times_list_12 = times_list[count-12:count]
    times_list_12_flo = [0,1,2,3,4,5,6,7,8,9,10,11]
    p=0
    while(p<12):
        times_list_12_flo[p] = float(times_list_12[p].strip())
        p=p+1
    min_12 = min(times_list_12_flo)
    max_12 = max(times_list_12_flo)
    p=0
    while(p<12):
      if(times_list_12_flo[p] == max_12 and max_c12 == 0):
         p=p+1
         max_c12 = 1
         continue
      if(times_list_12_flo[p] == min_12 and min_c12 == 0):
          p = p + 1
          min_c12 = 1
          continue
      avg12_flo = avg12_flo + (times_list_12_flo[p]/10)
      p = p+1
    avg12 = '%.2f' % (avg12_flo)
ao12 = Label(root, text = 'Average of 12: ' + avg12, font=20, background='#f6e58d', fg = 'black')
ao12.grid(row=5, column =1, pady=5, padx=10)
k = 0
mean = 0
while(k<count) :
    mean = mean + (float(times_list[k].strip()) / count)
    k = k+1
mean = '%.2f' % (mean)
meantotal = Label(root, text = 'Total Mean: ' + mean, font=20, background='#f6e58d', fg = 'black')
meantotal.grid(row=5, column =2, pady=5, padx=10)
root.title('pyCubeTimer')
root.mainloop()