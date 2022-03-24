from time import time  # keep track of time
import re
import csv
import random

# Source for quotes - https://gist.github.com/JakubPetriska/060958fd744ca34f099e947cd080b540

#Error function
def typeError(prompt):
    global input
    

    words = re.findall(r"[\w']+|[.,!?;]", prompt)

    print("prompt = ", words)
    print("output = ", input)

    error = input.copy()

    for i in range(len(input)):
        
        if (input[i] in words):
            error.remove(input[i])

    missed_word = abs(len(words) - len(input))
    res = missed_word + len(error)

    return res

def quotes():
    with open("quotes.csv") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)

    quote = data[random.randint(1, len(data) - 1)][1]

    return quote

#Speed function

def speed(inprompt, stime, etime):
    global time
    global input

    input = re.findall(r"[\w']+|[.,!?;]", inprompt)
    twords = len(input)
    speed = twords / time

    return speed

# Total time

def elapsedTime(stime, etime):
    time = etime - stime

    return time

if __name__ == "__main__":
    prompt = quotes()
    print("Type this: ", prompt)

    input("Press Enter then start typing: ")

    stime = time()
    inprompt = input()
    etime = time()

    time = round(elapsedTime(stime, etime), 2)
    speed = speed(inprompt, stime, etime)
    errors = typeError(prompt)

    #print the data
    print("#######################")
    print("Total time: ", time, "seconds")
    print("Average Typing Speed: ", speed, "words per minute")
    print("With total of ", errors, "errors.")
    print("#######################")