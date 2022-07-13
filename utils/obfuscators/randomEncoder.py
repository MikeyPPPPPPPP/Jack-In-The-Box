import base64
import random
import sys

class encoderGenrator:
	def __init__(self, text):
		self.text = text
		self.code = {}
		self.alpha = ['\t','\n',' ','!', '@', '~', '`', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '-', '+', '{', '}', '|', '\\', '}', '{', '[', ']', ':', ';', '"', "'", ',', '.', '/', '?', '>', '<', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'U', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		self.genrateKeys()
		self.encodeedText = (base64.b64encode(''.join([self.code[x] for x in self.text]).encode('ascii'))).decode('ascii')

	def genrateKeys(self):
		for x in self.alpha:
			self.randomCherector = self.alpha[random.randint(0,len(self.alpha)-1)]
			while True:
				if self.randomCherector not in [t[0] for t in self.code.values()]:#keys
					self.code[x]=self.randomCherector
					break
				else:
					self.randomCherector = self.alpha[random.randint(0,len(self.alpha)-1)]

	def codeGenrator(self):
		return 'import base64;exec(\'\'.join([y[0] for x in [x for x in base64.b64decode( (\''+self.encodeedText+'\').encode(\'ascii\') ).decode(\'ascii\')] for y in [[x[0], x[1]] for x in '+str(self.code)+'.items()] if x == y[1]]))'


#tcp = encoderGenrator('test')
#print(tcp.codeGenrator())

