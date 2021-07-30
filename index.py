import requests



for page in range(1,11):
  url = 'https://quotes.toscrape.com/page/' + str(page)
  r = requests.get(url)
  html = r.text
  print(html)
  with open('quotes.txt', 'a', encoding='utf-8') as f:
    for line in html.split('\n'):
      if '<span class="text" itemprop="text">' in line:
        line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
        line = line.strip()
        print(line)
        print('\n')
        f.write(line)
        f.write('\n')
        f.write('\n')
