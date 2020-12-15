import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.sainsburys.co.uk/gol-ui/SearchDisplayView?filters[keyword]=chicken%20breast&&langId=44&storeId=10151&searchType=2&searchTerm=chicken%20breast")
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

soupChildren = list(soup.children)
typesList = [type(item) for item in list(soup.children)]
htmlChildren = list(soupChildren[1])

soupParagraph = soup.find(class_="ln-o-section ln-o-section")
print(soupParagraph)