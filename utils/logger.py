import json 
import datetime
import os

PATH = "logs.json"
def log_event(event, data):
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "action": event,
        "data": data
    }

    if os.path.exists(PATH):
        with open(PATH, "r") as log_file:
            try:
                logs = json.load(log_file)
            except json.JSONDecodeError:
                logs = []  # If file is empty or invalid, start with empty list
    else:   
        logs = []

    logs.append(log_entry)

    with open(PATH, "w") as log_file:
        json.dump(logs, log_file, indent=4)