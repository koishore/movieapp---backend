import requests

imdbid = str(raw_input("Enter imdb id: "))
url = "http://www.omdbapi.com/?i=" + imdbid + "&type=movie&y=&plot=full&r=json"
s = requests.get(url).json()
print s['Poster']
print s['Plot']
