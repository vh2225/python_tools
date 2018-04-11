import bs4 as bs
import urllib.request
import os
import pandas as pd

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Use beautiful soup:
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# -----------------------------------------------------
# print(soup.title.text)
# print(soup.p) # first paragraph
# print(soup.find_all('p')) # all paragraph
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)
# print(soup.get_text())
# for url in soup.find_all('a'):
#     print(url.get('href'))

# -----------------------------------------------------
# nav = soup.nav
# for url in nav.find_all('a'):
#     print(url.get('href'))

# -----------------------------------------------------
# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

# -----------------------------------------------------
for div in soup.find_all('div', class_='body'):
    text = div.text
    text = os.linesep.join([s for s in text.splitlines() if s]) # this remove all empty lines
    print(text)

# -----------------------------------------------------
# table = soup.find('table') # same thing
table = soup.table
table_rows = table.find_all('tr')
data = []
for tr in table_rows:
    td = tr.find_all('td') # table data
    row = [i.text for i in td]
    if row: data.append(row) # the header would return an empty array
print(data)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# use pandas
# html5lib : pip install html5lib
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header = 0)
for df in dfs:
    print(df)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# use sitemap
sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(sauce, 'xml')
for url in soup.find_all('loc'):
    print(url.text)