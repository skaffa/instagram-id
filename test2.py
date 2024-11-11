import requests
from colorama import Fore, Style, init
import os
import base64 as b64

# Initialize colorama for colored output in the console
init(autoreset=True)

# Clear the screen for a clean start
os.system('cls||clear')

# ASCII art for branding
detective_ascii = """

Sorry, i deobfuscated the code.

"""

# Set the Instagram API endpoint URL for user lookup
final_url = 'https://i.instagram.com/api/v1/users/lookup/'

# Request for the target username
username = input(Fore.RED + "target" + Fore.WHITE + "@")

# Define the headers and data required for the POST request
headers = {
    'accept-language': 'en-US;q=1.0',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Instagram 337.0.3.23.54 (iPhone12,1; iOS 16_6; en_US; en; scale=2.00; 828x1792; 577210397) AppleWebKit/420+',
    'x-ig-app-id': '936619743392459',  # Instagram app ID
    'x-ig-www-claim': 'hmac.AR2yQATg0CNSYNr3DewbYrJfcN5Wf6xWWmZAzBb5zHl8u-RsQ3zjsIKoVQbGUh2YWeqs64F-LtQyEqFVlWs3IGXbdRvlV-Lexk0Abw_x4DRMf50hJAkTmoCq8E-tRu7dZX3A7I4RuLzMPn0Dp0fz60B5n4kW3sDOlcgGtoDvc5IzvhOzbU8U8kh_z2uh25wvAhP7aNlD5z6rQTxNmGRXjtnLByuYpvSzB57FcQ00Q==',
    'x-ig-www-claim': 'hmac.AR2yQATg0CNSYNr3DewbYrJfcN5Wf6xWWmZAzBb5zHl8u-RsQ3zjsIKoVQbGUh2YWeqs64F-LtQyEqFVlWs3IGXbdRvlV-Lexk0Abw_x4DRMf50hJAkTmoCq8E-tRu7dZX3A7I4RuLzMPn0Dp0fz60B5n4kW3sDOlcgGtoDvc5IzvhOzbU8U8kh_z2uh25wvAhP7aNlD5z6rQTxNmGRXjtnLByuYpvSzB57FcQ00Q==',
    'x-instagram-ajax': '1',
}

data = {"q": username}

# Try sending the request to the Instagram API and handling the response
try:
    response = requests.post(final_url, headers=headers, data=data)
    response.raise_for_status()  # Raises an exception for non-2xx status codes

    # Clear the console screen after request is made
    os.system('cls||clear')

    # Try parsing and outputting the response as JSON
    response_json = response.json()
    print(Fore.WHITE + "Response Details:")
    for key, value in response_json.items():
        print(f"{Fore.RED}{key.capitalize()}: {Fore.WHITE}{value}")

    # Get user data if available
    user = response_json.get('user', {})
    print(Fore.RED + "User Information:")
    print(Fore.RED + "  Full Name: " + Fore.WHITE + user.get('full_name', 'N/A'))
    print(Fore.RED + "  Username: " + Fore.WHITE + user.get('username', 'N/A'))
    print(Fore.RED + "  Profile Pic URL: " + Fore.WHITE + user.get('profile_pic_url', 'N/A'))
    print(Fore.RED + "  Verified: " + Fore.WHITE + str(user.get('is_verified', 'N/A')))

    # Wait for user input before closing the program
    input(Fore.RED + "Press Enter to close the program...")

except requests.exceptions.RequestException as e:
    print(Fore.RED + f"Error occurred: {e}")
