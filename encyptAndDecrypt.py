from cryptography.fernet import Fernet

class Message():

    def __init__(self, message):
        self.message = message

    def encryption(self, key):
        encodedMessage = self.message.encode()
        encrypted = key.encrypt(encodedMessage)
        self.message = str(encrypted).split('\'')[1]


    def decryption(self, key):
        try:
            decrypted = key.decrypt(self.message)
            decrypted = (str(decrypted)).split('\'')[1]
            self.message = decrypted
        except:
            print('Invalid decryption key provided')

# myHiddenMessage = 'This is a message'
#
#key = Fernet.generate_key()
# f = Fernet(key)
#
# m = Message(myHiddenMessage)
# m.encrypt(f)
# m.decrypt(f)
# print(m.message)
