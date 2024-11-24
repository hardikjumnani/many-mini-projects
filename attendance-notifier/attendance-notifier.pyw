from datetime import datetime
import time
from plyer import notification

datetime.now()

if __name__=="__main__":

    while True:
        time_now = datetime.now()

        if time_now.hour == 22 and time_now.minute == 30:
            notification.notify(
                title = "Hostel Attendance",
                message="Go mark your attendance!",
                timeout=2
            )

        time.sleep(60)