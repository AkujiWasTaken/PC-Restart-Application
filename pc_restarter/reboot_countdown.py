#import time module
import time
#import os
import os
#import win10toast
from win10toast import ToastNotifier

# define the countdown function
def shutdown_countdown_function(time_to_shutdown):
    try:
        while time_to_shutdown:
            mins, seconds = divmod(time_to_shutdown, 60)
            shutdown_timer = '{:02d}:{:02d}'.format(mins, seconds)
            print(shutdown_timer, end='\r')
            time.sleep(1)
            time_to_shutdown -= 1
            
            if time_to_shutdown == 3: #300 5 minutes in seconds
                #create an object to the ToastNotifier class
                notifier = ToastNotifier()
                notifier.show_toast("Shutdown Reminder:", "5 minutes until shutdown!", duration=10, icon_path='./restart_icon.ico')
        
        shutdown_options()
        
    except Exception as error:
        print("An error occurred while shutting down...")
        shutdown_countdown_function()
    except KeyboardInterrupt as key_interrupt:
        print("Controlled Shutdown...")
        

def shutdown_options():
    import os
    
    print("1. Launch Restart")
    print("2. Delay Restart by 15 minutes")
    print("3. Delay Restart by Custom Amount")
    print(end="Select Option: ")
    
    restart_selector = int(input())
    if restart_selector == 1:
        print("Launching Restart...")
        time.sleep(3.0)
        os.system("shutdown /r /t 0")
    
    elif restart_selector == 2:
        print("Restarting in 15 minutes...")
        time.sleep(3.0)
        os.system("shutdown /r /t 900")
    
    elif restart_selector == 3:
        print(end="Enter Number of Seconds to Delay Restart: ")
        seconds = int(input())
        strOne = "shutdown /r /t "
        strTwo = str(seconds)
        restart_string = strOne+strTwo
        os.system(restart_string)
    else:
        print("Invalid Choice...")
        
time_to_shutdown = 6 #28500 7 1/2 hours in seconds

if __name__ == '__main__':
    shutdown_countdown_function(int(time_to_shutdown))