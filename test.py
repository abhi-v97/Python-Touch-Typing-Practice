#file for quick code tests
from main import elapsedTime


prompt = "The quick brown fox jumped over the lazy dog"
print("Type this: ", prompt)

input("Press Enter to begin: ")

stime = time()
inprompt = input()
etime = time()

time = round(elapsedTime(stime, etime), 2)