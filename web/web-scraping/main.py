import csv
import requests
from bs4 import BeautifulSoup

STANDARD = 'https://www.foxsports.com/soccer/fifa-world-cup-men/team-stats?category=standard'
OFFENSIVE = 'https://www.foxsports.com/soccer/fifa-world-cup-men/team-stats?category=offensive'
DEFENSIVE = 'https://www.foxsports.com/soccer/fifa-world-cup-men/team-stats?category=defensive'
GOALKEEPING = 'https://www.foxsports.com/soccer/fifa-world-cup-men/team-stats?category=goalkeeping'

def scrape(url):
  html = requests.get(url).text
  soup = BeautifulSoup(html, 'html.parser')

  dicts = []
  for row in list(soup.select('.table-stats tr')):
    content = {}
    content['Team'] = row.select_one('a.table-entity-name').text.strip()

    i = 2
    for header in list(soup.select('.data-header th')[1:]):
      content[header.text.strip()] = ''.join(row.select_one(f'td[data-index="{i}"]').text.strip().split(','))
      i+=1
    
    dicts.append(content)
  
  return dicts

def writeCsv(dicts, filename):
  with open(filename+'.csv', 'w', newline='') as f:
    fieldnames = list(dicts[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dicts)


writeCsv(scrape(STANDARD), 'team-standard-stats')
writeCsv(scrape(OFFENSIVE), 'team-offensive-stats')
writeCsv(scrape(DEFENSIVE), 'team-defensive-stats')
writeCsv(scrape(GOALKEEPING), 'team-goalkeeping-stats')
