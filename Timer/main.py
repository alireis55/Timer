import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("Finish!")

seconds = input("How many seconds to count down? Enter an integer:")

while not seconds.isdigit():
    print("That wasn't an integer! Enter an integer!")
    seconds = input("How many seconds to count down? Enter an integer:")

seconds = int(seconds)

countdown(seconds)
