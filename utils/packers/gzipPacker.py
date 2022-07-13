import gzip
import sys

class packer:
	"""this class will pack a string using the gzip compression algorithm"""
	def __init__(self, text):
		self.text = text#this gets the filename

	def compressMe(self, data):
		"""returns a gzip compressed utf8 string"""
		return gzip.compress(data.encode()).decode('cp437')

	def deCompressMe(self, data):
		"""returns a decompressed string"""
		return gzip.decompress(data.encode('cp437')).decode()

	def returnString(self):
		code = self.compressMe(self.text).encode()
		readable = """
import gzip

code = """+str(code)+""".decode()
exec(gzip.decompress(code.encode('cp437')).decode())
"""
		return readable

#a = packer('test')
#print(a.returnString())

