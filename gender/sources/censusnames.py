''' Use the list of names from http://www.census.gov/genealogy/names/names_files.html to determine the gender of a given name
'''
import csv

#the format is name, male number, female number, total
_namesFcensus = [f for f in csv.reader(open('data/dist.female.first.txt'))]
_namesMcensus = [f for f in csv.reader(open('data/dist.male.first.txt'))]

# print(_namesFcensus) # Debugging
# print(_namesMcensus) # Debugging

# some pre-processing

for i in xrange(len(_namesFcensus)):
	row = _namesFcensus[i]
	row[0] = row[0].lower()
	row = row[0].split()
	row.append(0)
	_namesFcensus[i] = row
#	print row # Test

for i in xrange(len(_namesMcensus)):
	row = _namesMcensus[i]
	row[0] = row[0].lower()
	row = row[0].split()
	row.append(1)
	_namesMcensus[i] = row
#	print row # Test

_namesCensus = _namesFcensus + _namesMcensus
# print _namesCensus # Debugging

_threshold = 0.6

# print _names # Debugging

def gender(name):
	''' Return the gender of the given name, along with a confidence level
	Possible gender return values are:
	MALE
	FEMALE
	NEUTRAL
	UNKNOWN
	e.g. fbnames.getGender('alex') returns ('MALE',0.91...)
	fbnames.getGender('julie') reutrns ('FEMALE',0.95...)
	'''
	name = name.lower()
	try:
'''
		#first entry is the name, second is male number, 
		#third is female number, is last total
		malecount, femalecount = \
		[(row[1], row[2]) \
			for row in _names if row[0] == name][0]

		total = malecount + femalecount #just consider ppl that chose a gender
		if malecount > _threshold * total:
			return 'MALE', malecount / total
		elif femalecount > _threshold * total:
			return 'FEMALE', femalecount / total
		else:
			return 'NEUTRAL', 1 / (1 + abs(0.5 - malecount/total))
'''
	except IndexError: 
		return 'UNKNOWN',
