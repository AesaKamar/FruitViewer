#Uses CSS selectors to traverse DOM and organize Fruit DB
#Makes compatible with Rails seed data

from bs4 import BeautifulSoup
import os
import urllib2
import re
from imggrab import go #custom module to grab google images
import time


#parses table ftom TradeWinds to get fruit data
url = 'http://www.tradewindsfruit.com/content/fruitscommon.htm'
urlRoot = 'http://www.tradewindsfruit.com/content/'
content = urllib2.urlopen(url).read()

mainContent= BeautifulSoup(content)


#print mainContent.prettify()

section = mainContent.find_all('table')
#letter = section.find_all('tr')
class Fruit:
	def __init__(self, name):
		self.raw = name
		self.link = urlRoot + name + '.htm'
		self.name = name.replace('-', ' ').title().replace('/', "")
		# self.latinName
		# self.description
		# self.otherNames

		#grabs and polulates other data
		self.getData()

		#downloads other images from google
		#self.findImage(self.raw)

	def getData(self):
		#opens data as soup
		soup = BeautifulSoup(urllib2.urlopen(self.link).read())
		try:
			section = soup.find('div', {"class": "picture-sec"})
			#self.commonName=  str(section.find('h2'))[4:-5]
			self.latinName=  str(section.find('h3'))[4:-5]
			self.otherNames= str(section.find('span', {'class': 'style2'}))[27:-7]
			self.description = str(section.find('p',{'align': 'justify'}))[19:-4]
		except: 
			"error"
		time.sleep(1.5)
		

	def findImage(self, name):
		go(name, 'images')



f = open(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'/db/seeds.rb', 'w')
f.write('fruits = Fruit.create([')

fruits = {}


for letter in section:
	row = letter.find_all('a', href=True)
	for tag in row:
		name= tag['href'][:-4]
		if name[0]== '/':
			name = name[1:]

		print name
		fruits[name] =   Fruit(name)

		#writing to seeds.rb
		this = fruits[name]
		try:
			toWrite = "\n{name: '%s', latinName: '%s' , otherNames: \"%s\", description: \"%s\" , image: 'images/%s.jpg'}," % (this.name, this.latinName, this.otherNames, this.description.replace("\"", '\\\"'), name)
			f.write(toWrite)
		except AttributeError, e:
			print "stupid citrus..."
			continue

f.write('])')
f.close()

		


# fruits
# for key, value in fruits.items():
# 	print value.name