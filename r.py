import requests
from bs4 import BeautifulSoup
import sqlite3
response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')

#print(response.text)

soup = BeautifulSoup(response.text)
#print(soup.prettify())
#soup.table
print(soup.table)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE community
#             (cb text, area real, popcensus real, pop real, neighborhoods text)''')
purchases = [('b', 3, 4, 3, '45.00'),
             ('t', 2, 4, 3, '72.00'),
             ('c', 4, 4, 3, '53.00'),
            ]
c.executemany('INSERT INTO community VALUES (?,?,?,?,?)', purchases)
conn.commit()
conn.close()
conn = sqlite3.connect('example.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM community ORDER BY cb'):
        print(row)