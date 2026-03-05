from datetime import datetime
import os

def generate_log(data):
    
    if not isinstance(data, list):
        raise ValueError("Input must be a list of log entries.")

    
    today_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today_str}.txt"

    
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    
    print(f"Log written to {filename}")

    return filename