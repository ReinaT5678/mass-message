from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from twilio.rest import Client
import pytz

def send_message(target_numbers):
    # Twilio credentials
    account_sid = 'AC0bf1c0093e1690e87e08d49b642c263d'
    auth_token = 'dfbcc5a05c78b81be20b6efee20f7e83'
    twilio_number = '+18336754070'

    client = Client(account_sid, auth_token)

    for target_number in target_numbers:
        try:
            message = client.messages.create(
                body='Happy New Year! - Sent from a Python Script',
                from_=twilio_number,
                to=target_number
            )
            
            print(f"Message SID: {message.sid}")
            print(f"Message Status: {message.status}")

        except Exception as e:
            print(f"Error sending message to {target_number}: {e}")

# List of target phone numbers
target_numbers = ['+18083498800', '+8087630827']

# Set up the scheduler
scheduler = BackgroundScheduler()

# Specify the HST time zone
hawaii_tz = pytz.timezone('Pacific/Honolulu')

# Create a cron trigger for 12:00 AM on January 1st
cron_trigger = CronTrigger(month=1, day=1, hour=0, minute=0, second=0, timezone=hawaii_tz)


# Start the scheduler
scheduler.start()

# Keep the script running
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
