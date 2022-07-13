from cryptography.fernet import Fernet

class basicEncryption:
    def __init__(self, data):
        self.data = data

        self.mKey = Fernet.generate_key()
        self.encoded_message = self.data.encode()
        self.key = Fernet(self.mKey)
        self.encrypted_message = self.key.encrypt(self.encoded_message)

    def encrypt(self):
        poly = """
from cryptography.fernet import Fernet

encrypted_message = '"""+self.encrypted_message.decode()+"""'
key = """+str(self.mKey)+"""

f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message.encode())
exec(decrypted_message.decode())
        """
        return poly

#a = basicEncryption('test')
#s = a.encrypt()

