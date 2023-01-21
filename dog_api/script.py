import requests
import webbrowser



response = requests.get("https://dog.ceo/api/breeds/image/random")

if response.status_code == 200:
    webbrowser.open(response.json().get("message"))
