import time
from datetime import datetime, timedelta

while True:
    # Get the current date and time
    current_datetime = datetime.now()

    # Calculate the next logging time
    next_logging_time = current_datetime + timedelta(minutes=(5 - (current_datetime.minute % 5)))

    # Sleep until the next logging time
    sleep_duration = (next_logging_time - current_datetime).total_seconds()
    time.sleep(sleep_duration)

    # Get the current date and time again (in case it's time to log)
    current_datetime = datetime.now()

    # Get the current minute value
    current_minute = current_datetime.minute

    # Check if the current minute is one of the specified values
    if current_minute in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]:
        # Format the time as 'HH:MM'
        formatted_time = current_datetime.strftime("%H:%M")
        message = f"[{formatted_time}] Message for {formatted_time}."

        # Open the file in append mode and write the message
        with open("log.txt", "a") as file:
            file.write(message + "\n")

        print(f"Message has been written to the log.txt file: {message}")
