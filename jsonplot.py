from PIL import Image
import requests
import numpy as np
import urllib
import cv2

def urlimage(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	response = urllib.urlopen(url)
	image = np.asarray(bytearray(response.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	# return the image
	return image

imdbid = str(raw_input("Enter imdb id: "))
url = "http://www.omdbapi.com/?i=" + imdbid + "&type=movie&y=&plot=full&r=json"
s = requests.get(url).json()
print s['Poster']

if s['Poster'] != 'N/A':
    image = urlimage(s['Poster'])
    cv2.imshow("Image", image)
    cv2.waitKey(0)
else:
    print "No Poster Available!"
print
print s['Plot']
