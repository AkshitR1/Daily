import tkinter
import random

colors = ['Red','Blue','Black','White','Green','Purple','Yellow']

score = 0

rem_time = 45

def startg(event):

    if rem_time == 45 :
        countdown()
    
    nextcolor()

def nextcolor():
    
    global score
    global rem_time

    if rem_time > 0:

        e.focus_set()

        if e.get().lower() == colors[1].lower():

            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(colors)

        label.config(fg = str(colors[1], text = str(colors[0])))

        scoreLabel.config(text = "Score: "+ str(score))

def countdown():
    global rem_time

    if rem_time>0:

        rem_time -= 1

        timeLabel.config(text = "Time Remaining: "+ str(rem_time))

        timeLabel.after(1000,countdown)

root = tkinter.Tk()

root.title("Colours")

root.geometry("375x200")

instructions = tkinter.Label(root, text= "Type in the colour of the words , and not the word text!", font=('Helvetica', 12))

instructions.pack()

scoreLabel = tkinter.Label(root , text = "Press enter to begin", font=('Helvetica',12))

scoreLabel.pack()

timeLabel = tkinter.Label(root , text= "Time Left"+ str(rem_time), font =('Helvetica',12))

timeLabel.pack()

label = tkinter.Label(root, font = ('Helvetica',12))

label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startg)
e.pack()

e.focus_set()

root.mainloop()
