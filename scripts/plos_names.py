#!/usr/bin/python

import gender.plos_solr as plos
import gender.controller as c

authors = plos.singlefield('author',500) #pull up 500 articles

firstnames = []
for lst in authors:
	for a in lst:
		firstnames.append(a.split()[0])
print len(set(firstnames)), 'unique first names'
print len(firstnames), 'authors'

malecount = 0
femalecount = 0
neutralcount = 0
for name in firstnames:
	gender = c.majorityVote(name)
	if gender == 'MALE':
		malecount += 1
	elif gender == 'FEMALE':
		femalecount += 1
	elif gender == 'NEUTRAL':
		neutralcount += 1

print malecount, 'of the authors were male'
print femalecount, 'of the authors were female'
print neutralcount, 'of the authors had gender neutral names'

