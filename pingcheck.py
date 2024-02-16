import time
from datetime import datetime
from pythonping import ping
import requests


def send_msg(text):
    TOKEN = "6324490111:AAHpteJxsBl0i1yOYmrldxNX0P01A4YPR2Y"
    chat_id = "-4164702806"
    url_req = "https://api.telegram.org/bot" + TOKEN + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
    requests.get(url_req)

def ping_host(ip):
    response = ping(ip, count=1, timeout=1)
    return response.success()

def main():
    ip1 = "191.242.223.60"
    ip2 = "179.0.44.68"

    status1 = ping_host(ip1)
    status2 = ping_host(ip2)

    last_change_time = datetime.now()

    while True:
        time.sleep(5)
        new_status1 = ping_host(ip1)
        new_status2 = ping_host(ip2)

        current_time = datetime.now()

        if new_status1 != status1:
            status1 = new_status1
            if status1:
                send_msg(f"IP {ip1} (ALIVE) esta UP - {current_time.strftime('%H:%M:%S %d/%m/%Y')}")
            else:
                send_msg(f"IP {ip1} (ALIVE) esta DOWN - {current_time.strftime('%H:%M:%S %d/%m/%Y')}")
        
        if new_status2 != status2:
            status2 = new_status2
            if status2:
                send_msg(f"IP {ip2} (FLOPPY) esta UP - {current_time.strftime('%H:%M:%S %d/%m/%Y')}")
            else:
                send_msg(f"IP {ip2} (FLOPPY) esta DOWN - {current_time.strftime('%H:%M:%S %d/%m/%Y')}")

if __name__ == "__main__":
    main()
