import sys

#sys.path.append('../utils')

from utils.packers import gzipPacker
from utils.encoders import standard
from utils.obfuscators import randomEncoder, stringClass
from utils.encrypters import basicEncrypter



test = "print('hi')"


#base64 to  gzip    !!!!!!!!!
'''
s = standard.standardEncoding(test)
f = s.baseE64()
print(f)

t = gzipPacker.packer(f)
print(t.returnString())

'''
# gzip to base64  !!!!!!!!

'''
t = gzipPacker.packer(test)
f = t.returnString()

s = standard.standardEncoding(f)
print(s.baseE64())
'''


#gzip to poly
'''
t = gzipPacker.packer(test)
f = t.returnString()

s = randomEncoder.encoderGenrator(f)
print(s.codeGenrator())
'''


#gzip to encryptor
'''
t = gzipPacker.packer(test)
f = t.returnString()

s = basicEncrypter.basicEncryption(f)
print(s.encrypt())
'''

#gzip to stringclass
'''
t = gzipPacker.packer(test)
f = t.returnString()
s = stringClass.stringObjuscator(f)
print(s.obfuscat())
'''


# base64 to gzip to poly encoder to string class to encryptor !!!!!!!!!!!!!!!!!!!
'''
s = standard.standardEncoding(test)
f = s.baseE64()


t = gzipPacker.packer(f)
pa = t.returnString()



re = randomEncoder.encoderGenrator(pa)
ou = re.codeGenrator()

sc = stringClass.stringObjuscator(ou)
enc = sc.obfuscat()

ec = basicEncrypter.basicEncryption(enc)
print(ec.encrypt())
'''







