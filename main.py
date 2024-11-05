from requests import get
from bs4 import BeautifulSoup as bs4
import json
from colorama import init, Fore, Back

USER_AGENT = "Instagram 85.0.0.21.100 Apple (23/6.0.1; 538dpi; 1440x2560; LGE; LG-E425f; instagram; en_US"
USERNAME_TO_ID = "https://i.instagram.com/api/v1/users/web_profile_info/?username=*USERNAME*"
ID_TO_USERNAME = "https://i.instagram.com/api/v1/users/*USER_ID*/info/"
HEADERS = {
    "User-Agent": USER_AGENT,
    "Referer": "https://www.instagram.com/",
    }

init(autoreset=True)

def username_to_id(username):
    url = USERNAME_TO_ID.replace("*USERNAME*", username)
    response = get(url, headers=HEADERS)    
    try:
        j1 = json.loads(response.content)
        j2 = json.dumps(j1, indent=2)
        color = Fore.GREEN
    except:
        j2 = response.content
        color = Fore.RED

    print(f"{Back.BLACK}{color}{j2}")


def id_to_username(user_id):
    url = ID_TO_USERNAME.replace("*USER_ID*", user_id)
    response = get(url, headers=HEADERS)

    #not sure if this catch is accurate, since i haven't hit the rate limit yet on this endpoint
    try:
        j1 = json.loads(response.content)
        j2 = json.dumps(j1, indent=2)
        color = Fore.GREEN
    except:
        j2 = response.content
        color = Fore.RED

    print(f"{Back.BLACK}{color}{j2}")


# username_to_id("bldwhrr")
id_to_username("64633874089")
