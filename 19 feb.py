import time
import sys
import csv
from datetime import datetime
import winsound

def log_task(task):
    with open("work_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), task])

def start_timer(task_name, minutes=25):
    total_seconds = minutes * 60
    seconds = total_seconds
    print(f"\n--- Focus Session Started: {task_name} ---")
    
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            
            
            bar_length = 20
            progress = (total_seconds - seconds) / total_seconds
            filled = int(bar_length * progress)
            bar = '█' * filled + '-' * (bar_length - filled)
            
            # This line is essential to see the countdown!
            print(f"|{bar}| {mins:02d}:{secs:02d} Remaining", end="\r")
            
            time.sleep(1)
            seconds -= 1
            
        print(f"\n\n|{'█'*20}| Done! Time to stretch.")
        winsound.Beep(1000, 1000) 
        log_task(task_name)
        
    except KeyboardInterrupt:
        print("\n\nSession paused.")

if __name__ == "__main__":
    task_name = sys.argv[1] if len(sys.argv) > 1 else "Deep Work"
    start_timer(task_name)