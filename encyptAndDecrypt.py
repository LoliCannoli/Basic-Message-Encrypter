from cryptography.fernet import Fernet

class Message():

    def __init__(self, message):
        self.message = message

    def encrypt(self, key):
        encodedMessage = self.message.encode()
        encrypted = key.encrypt(message)
        self.message = encrypted

    def decrypt(self, key):
        try:
            decrypted = key.decrypt(self.message)
            decrypted = (str(decrypted)).split('\'')[1]
            self.message = decrypted
        except InvalidToken:
            print('Invalid decryption key provided')

myHiddenMessage = 'This is a message'

key = Fernet.generate_key()  # Store this key or get if you already have it
f = Fernet(key)

m = Message(myHiddenMessage)
m.encrypt(f)
m.decrypt(f)
print(m.message)
