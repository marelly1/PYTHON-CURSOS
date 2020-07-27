import requests
import feedparser

url="https://github.com/marelly1/PYTHON-CURSOS"
respuesta=requests.get(url)
print(respuesta.status_code)
#cuando la respuesta a este código es 200 significa que está ok
print()

html=respuesta.text
#print(html)
print(respuesta.json)
print()

headers=respuesta.headers
print(type(headers))
print(headers)
print()

print(respuesta.encoding)
print()

url = 'https://www.reddit.com/r/Python/.rss'
respuesta = feedparser.parse(url)
print(respuesta['feed']['title'])

print()

print(respuesta.headers)

print()

print(type(respuesta.entries))

for e in respuesta.entries:
    print(e.link)