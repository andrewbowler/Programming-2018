# Libraries
import urllib.request
import re

# Store URL HTML data as variable 'data'
data = urllib.request.urlopen('https://news.ycombinator.com/')
# Creates array 'headlines;' all text stored between designated headline tags for the site, turns bytes into a string
headlines = re.findall(r'"storylink">(.*?)</a>',data.read().decode('utf-8'))

# Creates a numbered list of each item in the array
for num, titles in enumerate(headlines):
	print(str(num + 1) + '. ' + titles)