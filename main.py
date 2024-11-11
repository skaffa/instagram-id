from requests import get
import json
from colorama import init, Fore, Back
import random
import sys
import os
import time

try:
    from json2html import *
    has_json2html = True
except:
    has_json2html = False
    print("json2html is not installed")
    print("The script will work fine, except for the optional HTML conversion")
    print("To install json2html: pip install json2html")


init(autoreset=True)

USERNAME_TO_ID = "https://i.instagram.com/api/v1/users/web_profile_info/?username=*USERNAME*"
ID_TO_USERNAME = "https://i.instagram.com/api/v1/users/*USER_ID*/info/"

USER_AGENTS = [
    "Instagram 123.1.0.26.115 Android (30/11; 320dpi; 720x1280; Xiaomi; Redmi Note 8; merlin; qcom; en_US; 190576963)", 
    "Instagram 157.0.0.37.120 Android (28/9; 320dpi; 720x1280; Samsung; SM-G960F; starlte; samsungexynos9810; en_US; 271682446)", 
    "Instagram 123.1.0.26.115 iPhone OS 14_0 (iPhone11,8; en_US; en-US; scale=2.00; 828x1792; 190541962)", 
    # no clue if using random useragents makes a difference, but i guess it wont hurt
]

HEADERS = {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept-Language": "en-US",
    "Accept-Encoding": "gzip, deflate",
    "X-IG-App-ID": "124024574287414",
    "X-IG-WWW-Claim": "0",
    "X-IG-Device-ID": "android-" + ''.join(random.choices("abcdef0123456789", k=16)),
    "X-Instagram-AJAX": "1",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://i.instagram.com/",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
}

COLOR = Back.BLACK + Fore.LIGHTYELLOW_EX

PRINT_USAGE = f"{Fore.LIGHTRED_EX}Usage: python main.py <id|username> <value>"

def username_to_id(username):
    url = USERNAME_TO_ID.replace("*USERNAME*", username)
    response = get(url, headers=HEADERS)

    if not check_if_valid_json(response.content):
        print(f"{COLOR}Error: {response.content}")
        return

    j1 = json.loads(response.content)
    j2 = json.dumps(j1, indent=2)

    print(f"{COLOR}{j2}")
    return j1


def id_to_username(user_id):
    url = ID_TO_USERNAME.replace("*USER_ID*", user_id)
    response = get(url, headers=HEADERS)

    if not check_if_valid_json(response.content):
        print(f"{COLOR}Error: {response.content}")
        return


    j1 = json.loads(response.content)
    j2 = json.dumps(j1, indent=2)

    print(f"{COLOR}{j2}")
    return j1

def outputToHTML(data, vtype, value):
    os.makedirs("output", exist_ok=True)

    userpart = f"{vtype.upper()[0:2]}_{value}"
    filename = f"output/{userpart}_{time.strftime('%d%m%Y_%H%M%S')}_R{random.randint(000000, 99999)}.html"
    html = json2html.convert(json=data)

    with open(filename, "w") as f:
        f.write(html)
        f.close()

    full_path = os.path.abspath(filename)

    print(f"{COLOR}HTML saved to {full_path}")

def check_if_valid_json(data):
    try:
        json.loads(data)
        return True
    except:
        return False

# username_to_id("bldwhrr")
# id_to_username("64633874089")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]

        if arg1.lower() == "id":
            cmd = id_to_username(arg2)
        elif arg1.lower() == "username":
            cmd = username_to_id(arg2)
        else:
            print(PRINT_USAGE)

        if has_json2html:
            convert = input(f"{Fore.YELLOW}Do you want to convert the JSON to HTML? (y/n) > ").lower()
            if convert == "y":
                outputToHTML(cmd, arg1, arg2)
            elif convert == "n":
                pass
            else:
                print("Bruh, thats neither yes nor no. I won't convert the json to HTML")


    else:
        print(PRINT_USAGE)