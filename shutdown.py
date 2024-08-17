import os
import time
from datetime import datetime, timedelta

# Function to schedule shutdown
def schedule_shutdown(shutdown_time):
    # Convert shutdown_time to a datetime object
    shutdown_time_today = datetime.strptime(shutdown_time, "%I:%M %p").replace(
        year=datetime.now().year,
        month=datetime.now().month,
        day=datetime.now().day
    )
    
    # Get the current time
    now = datetime.now()
    
    # If the shutdown time is earlier than or equal to the current time, schedule it for the next day
    if shutdown_time_today <= now:
        shutdown_time_today += timedelta(days=1)

    # Calculate the difference in seconds between now and the shutdown time
    time_diff = (shutdown_time_today - now).total_seconds()

    # Check if the time_diff is greater than 6 hours (21600 seconds)
    if time_diff > 21600:
        print("Error: The shutdown time is more than 6 hours from now. Please enter a closer time.")
        return
    
    # Wait until the specified time
    print(f"Computer will shut down in {time_diff} seconds")
    time.sleep(time_diff)
    
    # Shutdown the computer
    os.system("shutdown /s /f /t 0")

# Main function to get user input
def main():
    shutdown_time = input("Enter the time to shut down the computer (HH:MM AM/PM): ")
    
    # Validate time format
    try:
        datetime.strptime(shutdown_time, "%I:%M %p")
    except ValueError:
        print("Invalid time format! Please enter time in HH:MM AM/PM format.")
        return
    
    # Schedule the shutdown
    schedule_shutdown(shutdown_time)

if __name__ == "__main__":
    main()
