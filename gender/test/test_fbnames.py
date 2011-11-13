import unittest 
import gender.sources.fbnames as fbnames 
class TestFBNames(unittest.TestCase):
	def setUp(self):
		self.names = {
			'ALEX' : ('MALE', 0.9148671096345515),
			'JULIE' : ('FEMALE', 0.9989711934156379),
			'JIAMIN' : ('NEUTRAL', 1.0),
			'akal;;`~~' : ('UNKNOWN',)
		}
	def runTest(self):
		for name, result in self.names.iteritems():
			self.assertEqual((name, result), (name, fbnames.gender(name)))

if __name__ == '__main__':
	unittest.main()
