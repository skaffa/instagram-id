import requests
import json
import os
import random
import time
from requests import Session

# Define the paths for storing session data
SESSION_FILE = "session_data.json"

# User-Agent strings for rotation
USER_AGENTS = [
    "Instagram 123.1.0.26.115 Android (30/11; 320dpi; 720x1280; Xiaomi; Redmi Note 8; merlin; qcom; en_US; 190576963)", 
    "Instagram 157.0.0.37.120 Android (28/9; 320dpi; 720x1280; Samsung; SM-G960F; starlte; samsungexynos9810; en_US; 271682446)", 
    "Instagram 123.1.0.26.115 iPhone OS 14_0 (iPhone11,8; en_US; en-US; scale=2.00; 828x1792; 190541962)"
]

# Load or initialize session headers and cookies
def load_session_data(session):
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            session_data = json.load(f)
            session.headers.update(session_data.get("headers", {}))
            session.cookies.update(session_data.get("cookies", {}))

# Save session headers and cookies to a file
def save_session_data(session):
    session_data = {
        "headers": dict(session.headers),
        "cookies": session.cookies.get_dict()
    }
    with open(SESSION_FILE, "w") as f:
        json.dump(session_data, f)

# Initialize session with loaded headers and cookies, if available
session = Session()
load_session_data(session)

# Set headers including a randomized User-Agent
session.headers.update({
    "User-Agent": random.choice(USER_AGENTS),
    "Accept-Language": "en-US",
    "Accept-Encoding": "gzip, deflate",
    "X-IG-App-ID": "124024574287414",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://i.instagram.com/",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
})

# Example request function with persistent session data
def fetch_instagram_data(url):
    response = session.get(url)
    if response.status_code == 200:
        # Save session data to file after each successful request
        save_session_data(session)
        return response.json()
    elif response.status_code == 429:
        print("Rate limit reached. Please wait before retrying.")
        return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Example usage
username_url = "https://i.instagram.com/api/v1/users/web_profile_info/?username=exampleuser"
data = fetch_instagram_data(username_url)
if data:
    print("Fetched data:", json.dumps(data, indent=2))
