import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('Remaining time: ' + timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print('Time is up! Take a break.')

if __name__ == "__main__":
    try:
        minutes = int(input("Enter the focus time in minutes: "))
        focus_timer(minutes)
    except ValueError:
        print("Please enter a valid number of minutes.")
