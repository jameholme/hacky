#   Created 6/3/2020 by James Holmes

from bs4 import BeautifulSoup
import requests

def get_salt():
    #Define Headers/User-Agent so the server sends the full response
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    #The target URL
    url = "https://website"
    content = requests.get(url, headers=headers)
    soup = BeautifulSoup(content.text, "html.parser")
    #Finds all Input tags with the Name="" attribute, additional attributes can be added in the Dictionary 
    salt = soup.find("input", {"name":"VALUE"})
    #Returns the value we wanted in a string
    return salt.get("value")

if __name__ == "__main__":
    print(get_salt())
