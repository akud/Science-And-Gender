''' Use the list of names from  ... to determine the gender of a given name
'''
import csv

_names = [f for f in csv.reader(open('data/fbnames.csv'))]


def getGender(name):
	try:
		
