''' Use the list of names from  http://sites.google.com/site/facebooknamelist/namelist to determine the gender of a given name
'''
import csv

#the format is name, male number, female number, total
_names = [f for f in csv.reader(open('data/fbnames.csv'))]
_names = _names[1:len(_names)] #get rid of the header
#do some preprocessing
for row in _names:
	row[0] = row[0].lower()
	row[1] = float(row[1])
	row[2] = float(row[2])
	row[3] = float(row[3])

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
	except IndexError: 
		return 'UNKNOWN',
