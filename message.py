from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from twilio.rest import Client
import pytz

def send_message(target_numbers):
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    twilio_number = 'VERIFIED_TWILIO_NUM'

    client = Client(account_sid, auth_token)
    # List of target phone numbers
    target_numbers = ['LIST_NUM', 'LIST_NUM', 'LIST_NUM']

    for target_number in target_numbers:
        try:
            message = client.messages.create(
                body='Personal message! Happy new year!',
                from_=twilio_number,
                to=target_number
            )
            
            print(f"Message SID: {message.sid}")
            print(f"Message Status: {message.status}")

        except Exception as e:
            print(f"{target_number} Error: {e}")


scheduler = BackgroundScheduler()

# change to specify your timezone here
hawaii_tz = pytz.timezone('Pacific/Honolulu')

# Cron trigger for 12:00 AM on January 1st
cron_trigger = CronTrigger(month=1, day=1, hour=0, minute=0, second=0, timezone=hawaii_tz)
scheduler.start()

# Continuous script after running using python3 file_name.py &
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
