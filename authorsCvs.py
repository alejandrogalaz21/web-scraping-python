import csv
import requests

url = 'https://quotes.toscrape.com/'
tag = '<span>by <small class="author" itemprop="author">'
endTag ='</small>'

response = requests.get(url)
html = response.text

# open the file in the write mode
with open('authors.csv', 'w', encoding='UTF8') as file:
  # create the csv writer
  writer = csv.writer(file)
  for line in html.split('\n'):
    if tag in line:
      line = line.replace(tag, '').replace(endTag, '')
      line = line.strip()
      print([line])
      # write a row to the csv file
      writer.writerow([line])
  file.close()      