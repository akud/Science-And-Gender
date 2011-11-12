import unittest
import gender.sources.fbnames as fbnames

class TestFBNames(unittest.TestCase):
	def setUp(self):
		self.names = {
			'ALEX' : ('MALE', 0.4431703882518608),
			'JULIE' : ('FEMALE', 0.4114406779661017),
			'akal;;`~~' : ('UNKNOWN',)
		}
	def runTest(self):
		for name, result in self.names.iteritems():
			self.assertEqual(result, fbnames.getGender(name))

if __name__ == '__main__':
	unittest.main()
