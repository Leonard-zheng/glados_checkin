import os
import requests

def checkin(user_label,  cookie):
    url = "https://glados.cloud/api/user/checkin"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": cookie,
        "Origin": "https://glados.space",
        "Referer": "https://glados.space/console/checkin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0 Safari/537.36"
    }
    data = {
        "token": "glados.one"
    }

    response = requests.post(url, headers=headers, json=data)
    print(f"=== {user_label} ===")
    print("Status:", response.status_code)
    try:
        print("Response:", response.json())
    except:
        print("Raw Response:", response.text)
    print("")


checkin("User (Me)", os.environ.get("GLADOS_COOKIE"))
