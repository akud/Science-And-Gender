# library for handling http request for Ushahidi API JSON data
import httplib
import csv

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
for row in _catsF:
	# store a connection
	conn = httplib.HTTPConnection("en.wikipedia.org")
	# write the correct url
	caturl = "/w/api.php?action=query&list=categorymembers&cmnamespace=0&cmlimit=100&cmtitle=Category:" + str(row[0])
#	print caturl # Debugging
	# form the request
	conn.request("GET", caturl)
	# store the response
	r1 = conn.getresponse()
	# add this to our running tally of dump
#	_namesFdump = _namesFdump + [r1.read()]
	print r1.read()

# print _namesFdump

# actually get info, store in a variable
# r1 = conn.getresponse()
''' print r1.status, r1.reason # Debugging'''
# use read() to get data, store in variable
# postsJSON = r1.read()
# print postsJSON # Debugging

# try to import json library, if can't, import alternative simplejson
try:
    import json
except ImportError:
    import simplejson as json

# use json.loads() to parse the JSON data into something python-readable
postsParsed = json.loads(postsJSON)
# print postsParsed # Debugging

# sampleCaption = postsParsed[u'response'][u'posts'][1][u'caption'] # Debugging
# print sampleCaption # Debugging

# function to return "captions" from python-readable data.
def captions(posts):
    allCaptions = '' # Var to store the full list
    justPosts = postsParsed[u'response'][u'posts'] # Var to grab just the post objects
    for r in justPosts:
        allCaptions = allCaptions + r[u'caption']
    return allCaptions

# print returned captions
# print(captions(postsParsed))

# newfile = open('text.txt', mode="w")
# newfile.write(captions(postsParsed))

