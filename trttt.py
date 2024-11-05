from requests import get
from bs4 import BeautifulSoup as bs4
import json
from colorama import init, Fore, Back, Style

USER_AGENT = "Instagram 85.0.0.21.100 Android (23/6.0.1; 538dpi; 1440x2560; LGE; LG-E425f; vee3e; en_US"
# ID_TO_USERNAME = "https://i.instagram.com/api/v1/users/*USER_ID*/info/"
# USERNAME_TO_ID = "https://www.instagram.com/*USERNAME*/?__a=1"
USERNAME_TO_ID = "https://i.instagram.com/api/v1/users/web_profile_info/?username=*USERNAME*"
HEADERS = {"User-Agent": USER_AGENT}

init(autoreset=True)

def username_to_id(username):
    url = USERNAME_TO_ID.replace("*USERNAME*", username)
    response = get(url, headers=HEADERS)
    print(response.status_code)
    
    j1 = json.loads(response.content)
    j2 = json.dumps(j1, indent=2)

    return j2

print(f"{Fore.GREEN}{username_to_id("bldwhrr")}")







# find user by id
# find user by username