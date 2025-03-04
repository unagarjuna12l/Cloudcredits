import time
import datetime
import winsound  # For Windows users; use an alternative for Linux/Mac

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            winsound.Beep(2500, 1000)  # Beeps at 2500 Hz for 1 second (Windows only)
            break
        time.sleep(1)  # Check time every second

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS format, 24-hour): ")
    set_alarm(alarm_time)
