import csv
import requests

url = 'https://www.heb.com.mx/super/abarrotes'
tag = '\'name\': "'
endTag = '",'

response = requests.get(url)
html = response.text

# open the file in the write mode
with open('csv_file.csv', 'w', encoding='UTF8') as file:
  for line in html.split('\n'):
    if tag in line:
      line = line.replace(tag, '').replace(endTag, '')
      line = line.strip()
      print(line)
      # create the csv writer
      writer = csv.writer(file)
      # write a row to the csv file
      writer.writerow([line])