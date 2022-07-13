import base64
import codecs

class standardEncoding:
    def __init__(self, text):
        self.text = text

    def baseE64(self):#might return a byte object
        eText = base64.b64encode(str(self.text).encode())
        return """import base64
exec(base64.b64decode("""+str(eText)+""").decode())"""

    def hexE(self):
        eText = codecs.encode(self.text.encode(), "hex")
        return """
import codecs
exec(codecs.decode("""+str(eText)+""", "hex").decode())"""

    def binE(self):
        pass


#t = standardEncoding('test')
#print(t.hexE())