import urllib2 as url
import csv, json

# get list of categories, store as variables
_catsF = [f for f in csv.reader(open('data/categories/wikipedia_fname_categories.csv'))]
_catsM = [f for f in csv.reader(open('data/categories/wikipedia_mname_categories.csv'))]
_catsU = [f for f in csv.reader(open('data/categories/wikipedia_uname_categories.csv'))]

# store connection
# conn = httplib.HTTPConnection("en.wikipedia.org")

# create variable to store all the requested names

# _namesFdump = []
_namesList = []

# pass values for API request to get json response
# But need to loop through all the categories
def getNamesFromCat(categoryList):
	for row in categoryList:
		# store a connection
		caturl = "http://en.wikipedia.org/w/api.php?format=json&action=query&list=categorymembers"+\
			"&cmnamespace=0&cmlimit=100&cmtitle=Category:" + url.quote(row[0])
		postsParsed = json.load(url.urlopen(caturl))
#		print json.dumps(postsParsed,indent=2)
#		_namesFdump = _namesFdump + [postsParsed]
		for n in xrange(len(postsParsed[u'query'][u'categorymembers'])):
			nameParens = postsParsed[u'query'][u'categorymembers'][n][u'title']
#			print nameParens

			if nameParens.find('(') != -1: 
				nameParens = nameParens[0:nameParens.find('(')]
#			print nameParens
			_namesList.append(nameParens)

def getAndWriteNames(categoryList, fileName):
	getNamesFromCat(categoryList)
	for n in xrange(len(_namesList)):
		_namesList[n] = _namesList[n].encode('ascii', 'ignore') # convert unicode to ascii
	f = file('data/'+fileName+'.txt', 'w')
	text = '\n'.join(_namesList)
	f.write(text)

getAndWriteNames(_catsF, 'wikiFemaleNames')
getAndWriteNames(_catsM, 'wikiMaleNames')
getAndWriteNames(_catsU, 'wikiUniNames')

# save to csv
'''testfile = open('data/testfile.csv', 'wb')
wr = csv.writer(testfile, quoting=csv.QUOTE_ALL)
wr.writerow(_namesFlist)
'''

# change to ascii from unicode
#for n in xrange(len(_namesFlist)):
#	_namesFlist[n] = _namesFlist[n].encode('ascii', 'ignore')

# save to a text file
#f = file('data/wikiFemaleNames.txt', 'w')
#text = '\n'.join(_namesFlist)
#f.write(text)

# print _namesFlist # Debugging

