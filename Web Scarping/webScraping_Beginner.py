import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract quotes
quotes = soup.find_all("span", class_="text")

for quote in quotes:
    print(quote.text)

print('Hello')