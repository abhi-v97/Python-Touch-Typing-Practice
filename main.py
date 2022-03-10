from time import time  # keep track of time

#Error function
def typeError(prompt):
    global inwords

    error = 0
    words = prompt.split()

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                error += 1
        else:
            if inwords[i] == words[i]:
                continue
            else:
                error += 1

    return error

#Speed function

def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time

    return speed

# Total time

def elapsedTime(stime, etime):
    time = etime - stime

    return time


prompt = "The quick brown fox jumped over the lazy dog"
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