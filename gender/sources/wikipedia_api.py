import urllib2 as url
import csv, json

# get list of categories, store as variables
_catsF = [f for f in csv.reader(open('data/categories/wikipedia_fname_categories.csv'))]
_catsM = [f for f in csv.reader(open('data/categories/wikipedia_mname_categories.csv'))]
_catsU = [f for f in csv.reader(open('data/categories/wikipedia_uname_categories.csv'))]

# store connection
# conn = httplib.HTTPConnection("en.wikipedia.org")

# create variable to store all the requested names

_namesFdump= []

# pass values for API request to get XML response
# But need to loop through all the categories
for row in _catsF[0:2]:
	# store a connection
	caturl = "http://en.wikipedia.org/w/api.php?format=json&action=query&list=categorymembers"+\
		"&cmnamespace=0&cmlimit=100&cmtitle=Category:" + url.quote(row[0])
	postsParsed = json.load(url.urlopen(caturl))
	print json.dumps(postsParsed,indent=2)


def captions(posts):
	'''Return "captions" from python-readable data.
	'''
	allCaptions = '' # Var to store the full list
	justPosts = postsParsed[u'response'][u'posts'] # Var to grab just the post objects
	for r in justPosts:
		allCaptions = allCaptions + r[u'caption']
	return allCaptions
