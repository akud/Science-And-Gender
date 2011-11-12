''' Use the list of names from  ... to determine the gender of a given name
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


def getGender(name):
	name = name.lower()
	try:
		#first entry is the name, second is male number, third female number, last total
		maleproportion, femaleproportion = \
		[(row[1] / row[3] , row[2] / row[3]) \
			for row in _names if row[0] == name][0]
		if maleproportion  > femaleproportion:
			return 'MALE', maleproportion
		elif femaleproportion > maleproportion:
			return 'FEMALE', femaleproportion
		else:
			return 'NEUTRAL',
	except IndexError: 
		return 'UNKNOWN',
