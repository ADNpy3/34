import schedule
import time
import os
# Define a function to print a message


def print_message():
    os.system ("chmod +xwr s3.sh")
    os.system ("./s3.sh")


# Schedule the task to run every day at 7:00 AM
schedule.every().day.at("14:10:00").do(print_message)

while True:
    schedule.run_pending()
    time.sleep(1)

