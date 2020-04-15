import requests
from bs4 import BeautifulSoup

print('Beginning file download...')

url = 'https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset/download'
r = requests.get(url, allow_redirects=True)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

print("HTTP status code:",r.status_code)
print("Content type:", r.headers['content-type'])
