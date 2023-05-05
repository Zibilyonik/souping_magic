import requests

from bs4 import BeautifulSoup
def magicker():
    magic_word = input()
    magic_url =input()
    page = requests.get(magic_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    big_text = soup.getText()
    for line in big_text:
        if magic_word in line:
            print(line)
            return        
magicker()
