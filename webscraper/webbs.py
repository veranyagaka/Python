import requests
from bs4 import BeautifulSoup
import csv
url = 'https://www.nytimes.com'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.title.text.strip()

print(f"Title of the website '{url}': {title}")
meta_description = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else 'Description not found'
print(meta_description)
links = [link.get('href') for link in soup.find_all('a', href=True)]
article_headlines = [headline.text.strip() for headline in soup.find_all('h2', class_='css-1vvhd4r e1voiwgp0')]

csv_file = 'nytimes_data.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL', 'Title', 'Meta Description'])
    writer.writerow([url, title, meta_description])

    writer.writerow(['Links'])
    for link in links:
        writer.writerow([link])

    writer.writerow(['Article Headlines'])
    for headline in article_headlines:
        writer.writerow([headline])

print(f"Data extracted and saved to {csv_file}")