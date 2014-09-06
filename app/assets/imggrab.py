import json
import os
import time
import requests
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError
 
def go(query, path):
  """Download full size images from Google image search.
 
  Don't prinst or republish images without permission.
  I used this to train a learning algorithm.
  """
  BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
             'v=1.0&q=' + query+ '-fruit' + '&start=%d'

 
  BASE_PATH = os.path.join('images')
 
  if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)
  start = 0 # Google's start query string parameter for pagination.
  while start < 5: # Google will only return a max of 56 results.
    r = requests.get(BASE_URL % start)
    try:
      for image_info in json.loads(r.text)['responseData']['results']:
        url = image_info['unescapedUrl']
        try:
          image_r = requests.get(url)
        except ConnectionError, e:
          print 'could not download %s' % url
          continue
      
        # Remove file-system path characters from name.
        title = image_info['titleNoFormatting'].replace('/', '').replace('\\', '')
   
        file = open(os.path.join(BASE_PATH, '%s.jpg') % query, 'w')
        try:
          Image.open(StringIO(image_r.content)).save(file, 'JPEG')
        except IOError, e:
          # Throw away some gifs...blegh.
          print 'could not save %s' % url
          continue
        finally:
          file.close()
        break # ends after one iteration
        #I don't know how to make JSON only request one object
    except TypeError,  e:
      print 'could not find image of %s' % query
      time.sleep(20)
      continue
      #print start
      start += 1 # 4 images per page.
   
      # Be nice to Google and they'll be nice back :)
      time.sleep(1.5)
  
# Example use
#go('orange', 'myDirectory')
