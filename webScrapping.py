import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input Github Username : ")
url = "https://github.com/"+github_user
r = requests.get(url)
soup = bs(r.content, "html.parser")
profile_image = soup.find("img", {"alt": "Avatar"})["src"]
print("This is the link to profile image of given github account", profile_image)
