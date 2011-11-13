''' Use the list of names from  http://en.wikipedia.org/wiki/Category:Given_names_by_gender to determine the gender of a given name
'''
import csv

# the format is name, male number, female number, total
_namesFemale = [f for f in csv.reader(open('data/wikipedia_names_female.csv'))]
_namesMale = [f for f in csv.reader(open('data/wikipedia_names_male.csv'))]

# print _namesFemale # Debugging
# print _namesMale # Debugging

# _names = _names[1:len(_names)] #get rid of the header

# need to do just a bit of preprocessing, make lower-case

for n in _namesFemale:
	n[0] = n[0].lower()
        n.append(0)
#	print n # Debugging
for n in _namesMale:
	n[0] = n[0].lower()
	n.append(1)
#	print n # Debugging

# combine lists
_namesCombined = _namesFemale + _namesMale
print _namesCombined # Debugging

def gender(name):
	''' Return the gender of the given name, but no confidence level
	Possible gender return values are:
	MALE
	FEMALE
	NEUTRAL # Except this one...
	UNKNOWN
	e.g. fbnames.getGender('alex') returns ('MALE', 0)
	fbnames.getGender('julie') returns ('FEMALE', 0)
	'''
        name = name.lower()
	try:
		#first entry is the name, second is male number, 
		#third is female number, is last total

		for n in _namesCombined:
			if n[0] == name:
#				print n[0] # Debugging
				if n[1] == 0:
					return 'FEMALE', 0
				elif n[1] == 1:
					return 'MALE', 0
				else:
					return 'UNKNOWN', 0
		return 'UNKNOWN', 0
	except IndexError: 
		return 'UNKNOWN', 0

# print(gender('Aaron')) # Testing
# print(gender('Aila')) # Testing

