import requests
import schedule
import time

def send_message():
    resp = requests.post("https://textbelt.com/text", {
        "phone": "+1503429876",
        "message": "Hello, world!",
        "key": "textbelt" # Replace with your own TextBelt API key!
    })
    print(resp.json())
    
schedule.every().day.at('10:30').do(send_message)