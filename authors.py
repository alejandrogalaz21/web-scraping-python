import requests

r = requests.get('https://quotes.toscrape.com/')

html = r.text
tag = '<span>by <small class="author" itemprop="author">'
endTag ='</small>'

with open('authors.txt', 'w') as f:
  for line in html.split('\n'):
    if tag in line:
      line = line.replace(tag, '').replace(endTag, '')
      line = line.strip()
      print(line)
      f.write(line)
      f.write('\n')
