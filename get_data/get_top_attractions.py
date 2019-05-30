from urllib.request import urlopen

html = urlopen('https://www.timeout.com/dublin/things-to-do/best-things-to-do-in-dublin')
print(html.read())
