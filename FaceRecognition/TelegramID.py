import requests

# Replace 'YOUR_API_TOKEN' with the token provided by the BotFather
API_TOKEN = 'Paste your API'
url=f"https://api.telegram.org/bot{API_TOKEN}/getUpdates"
print(requests.get(url).json())