from http import client
from tkinter import *
import ctypes
import random
import tkinter
import csv

# Source for quotes - https://gist.github.com/JakubPetriska/060958fd744ca34f099e947cd080b540

# For a sharper window
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# colours for text and bg
text_c = "#5f6368"
label_c = "teal"
bg_c = "#f1f3f4"

# Setup
root = Tk()
root.title('Typing Speed Practice')
root.geometry('700x700')
root.configure(bg=bg_c)

# font for labels and buttons
# consolas for readability, same font as VScode
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")
maxWPM = 0


# function triggered when any keyboard key is pressed
def keyPress(event=None):
    global firstKey, mistake
    try:
        if firstKey == 0: 
            # start timer after the user has started typing
            root.after(1000, startTimer)
            firstKey = 1
    
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # remove letter frp, right side
            labelRight.configure(text=labelRight.cget('text')[1:])
            # push it to the left
            labelLeft.configure(text=labelLeft.cget(
                'text') + event.char.lower())
            # get the next letter in queue
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
        else:
            # if pressed key doesn't match, its a mistake
            mistake += 1
            # print("FOO")
    except tkinter.TclError:
        pass
    except IndexError:
        # when the quote has ended, stop the test
        root.after(0, stopTest(event))

# Take a random quote from an absurdly large list
def quotes():
    with open("quotes.csv") as f:
        # take the quotes, place them in reader
        reader = csv.reader(f, delimiter=",")

        # convert them into a list
        data = list(reader)

    quote = data[random.randint(1, len(data) - 1)][1]

    return quote

# Initial screen, generates widgets for writing
# reset to zero every time the function is called
def resetWritingLabels():
    
    # Reset variables to zero, useful after hitting retry
    global firstKey, mistake
    firstKey = 0
    mistake = 0

    # grab quote
    text = quotes().lower()

    text = "the quick brown fox jumped over the lazy dog"

    # defines the point where the text splits
    splitPoint = 0

    # Instructions
    global HeaderHabel
    HeaderHabel = Label(root, text="Start Typing!", fg=text_c, bg=bg_c)
    HeaderHabel.place(relx=0.5, rely=0.2, anchor=CENTER)

    # Text that has been correctly typed
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg="#a5a6a7", bg=bg_c)
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    # Text remaining to type
    global labelRight
    labelRight = Label(root, text=text[splitPoint:], fg=text_c, bg=bg_c)
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    # The next letter to press
    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg=text_c, bg=bg_c)
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    # Timer widget
    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 seconds', fg=text_c, bg=bg_c)
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)
    root.bind('<Return>', stopTest)

    # Used for the timer, in startTimer function
    global passedSeconds
    passedSeconds = 0

# Function that triggers when the test is finished
def stopTest(event):

    # writeAble disables key press event after the test is over
    # also controls the timer
    global writeAble, wpm
    wpm = 0
    writeAble = False

    # words typed
    amountWords = len(labelLeft.cget('text').split(' '))

    # Remove unwanted widgets, so they don't overlap with the new widgets
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    # labels used to display results as a formatted string
    global ResultLabel, WordLabel, TimeLabel, misLabel, maxWPM, maxLabel

    # used to get the high score
    try:
        wpm = (amountWords / passedSeconds) * 60
        maxWPM = max(maxWPM, wpm)
    except ZeroDivisionError:
        pass

    #print(wpm, amountWords, passedSeconds)
    maxLabel = Label(
        root, text=f'High Score: {"{:.2f}".format(maxWPM)} wpm', fg=text_c, bg=bg_c)
    maxLabel.place(x=4.0, y=0.0)

    TimeLabel = Label(
        root, text=f'Time Taken(s): {passedSeconds}', fg=text_c, bg=bg_c)
    TimeLabel.place(relx=0.5, rely=0.2, anchor=CENTER)

    WordLabel = Label(
        root, text=f'Typed Words: {amountWords}', fg=text_c, bg=bg_c)
    WordLabel.place(relx=0.5, rely=0.3, anchor=CENTER)

    ResultLabel = Label(
        root, text=f'Words per Minute(wpm): {"{:.2f}".format(wpm)}', fg=text_c, bg=bg_c)
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    misLabel = Label(root, text=f'Mistakes: {mistake}', fg=text_c, bg=bg_c)
    misLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    # button to restart the game
    global ResultButton
    ResultButton = Button(root, text=f'Retry',
                          command=restart, bg="#107895", fg="#f1f3f4")
    ResultButton.place(relx=0.5, rely=0.8, anchor=CENTER)


def restart():
    # Remove the result widgets
    ResultLabel.destroy()
    ResultButton.destroy()
    WordLabel.destroy()
    TimeLabel.destroy()
    misLabel.destroy()
    maxLabel.destroy()

    # go back to start of program
    resetWritingLabels()


def startTimer():
    try:
        global passedSeconds
        passedSeconds += 1
        timeleftLabel.configure(text=f'{passedSeconds} Seconds')

        # call this function again after one second if the test is not over
        if writeAble:
            root.after(1000, startTimer)
    except TclError:
        pass

# setup the test
resetWritingLabels()

# Start mainloop
root.mainloop()
