import requests
r = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
r.headers['content-type']
r.encoding
r.text
r.json()
json = r.json()
response = json['insult']
print (response)
