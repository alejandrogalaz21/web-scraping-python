import csv
import requests

url = 'https://quotes.toscrape.com/'
authorTag = '<span>by <small class="author" itemprop="author">'
authorEndTag ='</small>'

quoteTag = '<span class="text" itemprop="text">“'
quoteEndTag = '”</span>'

for page in range(1,11):
  url = 'https://quotes.toscrape.com/page/' + str(page)
  response = requests.get(url)
  html = response.text
  # open the file in the write mode
  with open('authors.csv', 'w', encoding='UTF8') as file:
    # create the csv writer
    writer = csv.writer(file)
    for line in html.split('\n'):
      # quote
      if quoteTag in line:
        quote = line.replace(quoteTag, '').replace(quoteEndTag, '').strip()  
      # author
      if authorTag in line:
        author = line.replace(authorTag, '').replace(authorEndTag, '').strip()
        # print vars
        print([quote, author])    
        # write a row to the csv file
        writer.writerow([author, quote])
    file.close()      