from bs4 import BeautifulSoup

with open('/home/nabin/Documents/python/day7/sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
# match = soup.title.text
# match = soup.find('div', class_="footer")
# print(match)

for article in soup.find_all('div', class_="article"):
    headline = article.h2.a.text
    summary = article.p.text
    print(headline, summary)
