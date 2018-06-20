'''
Define a custom exception class
which takes a string message as attribute.
'''

class MyError(Exception):
	def __init(self, msg):
		self.msg = msg
error = MyError("Something Wrong")