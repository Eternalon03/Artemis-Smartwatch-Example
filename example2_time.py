
from Artemis import * 
from Circuitos import BM8563
import sys
import time

begin()

class Time:
    year = 0
    month = 0
    day = 0
    hours = 0
    minutes = 0
    seconds = 0
    
# Create a Time object and fill it with the current date/time
current = Time()
current.year = 2026
current.month= 3
current.day = 23
current.hours = 13
current.minutes = 33
current.seconds = 46

# Send it to the hardware chip
rtc.set_time (current)




while True:

    # 1. Ask the RTC chip for the live time 
    live_time = rtc.get_time()
    # 2. Extract hours, minutes, and seconds
    h = live_time.hours
    m = live_time.minutes
    s = live_time.seconds
    
    # Convert 24-hour time to 12-hour AM/PM format 
    ampm = "AM"
    if h >= 12:
        ampm= "PM"
    if h > 12:
        h = 12
    if h == 0:
        h = 12

    # 3. Format with leading zeros (e.g., 05 instead of 5) 
    time_string=f" (h): (m: 02d):{s: 02d} {ampm}" 
    date_string=f"{live_time.month}/{live_time.day}/{live_time.year}"

    # 4. Draw display.
    display.fill(0)
    display.text("ARTEMIS OS", 25, 10, Display. Color.Cyan)
    display.text(time_string, 15, 55, Display. Color.White)
    display.text(date_string, 25, 75, Display. Color.Yellow) 
    
    display.commit()

    # Only update twice a second to save battery and prevent flickering 
    time.sleep_ms(500)