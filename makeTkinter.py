from tkinter import *
from encyptAndDecrypt import Message
from cryptography.fernet import Fernet

def makeWindow():
    window = Tk()
    window.resizable(0,0)
    window.geometry("675x350")

    def Encrypt():

        key = keyText.get(1.0, 'end').strip()
        message = messageText.get(1.0, 'end').strip()

        if(message == 'None or invalid message'):
            return

        if key and message:
            message = Message(message)

            try:
                key = Fernet(key.encode())
            except base64.binascii.Error:
                keyText.delete(1.0, 'end')
                keyText.insert(1.0, 'Invalid Key')
                return

            message.encryption(key)

            messageText.delete(1.0, 'end')
            messageText.insert(1.0, message.message)

        if not message:
            messageText.insert(1.0, 'None or invalid message')
        if not key:
            keyText.insert(1.0, 'None or invalid key')

    def Decrypt():

        key = keyText.get(1.0, 'end').strip()
        message = messageText.get(1.0, 'end').strip()

        if(message == 'None or invalid message'):
            return

        if key and message:
            message = Message(message.encode())

            try:
                key = Fernet(key.encode())

            except base64.binascii.Error:
                keyText.delete(1.0, 'end')
                keyText.insert(1.0, 'Invalid Key')
                return

            message.decryption(key)

            messageText.delete(1.0, 'end')
            messageText.insert(1.0, message.message)

        if not message:
            messageText.insert(1.0, 'None or invalid message')
        if not key:
            keyText.insert(1.0, 'None or invalid key')

    def generateKey():
        key = str(Fernet.generate_key()).split('\'')[1]
        keyText.delete(1.0, 'end')
        keyText.insert(1.0, key)
        
    buttonFrame = Frame(window).pack(side = BOTTOM)
    inputFrame = Frame(window).pack(side = TOP)


    messageTextLabel = Label(inputFrame, text = 'Your message:').pack()
    messageText = Text(height = 7)
    messageText.pack()

    keyTextLabel = Label(inputFrame, text = 'Your Key:').pack()
    keyText = Text(height = 2)
    keyText.pack()


    encryptButton = Button(buttonFrame, text = 'Encrypt', width = 25, height = 5, command = Encrypt).pack(side = LEFT)
    generateButton = Button(buttonFrame, text = 'Generate Key', width = 25, height = 5, command = generateKey).pack(side = LEFT)
    decryptButton = Button(buttonFrame, text = 'Decrypt', width = 25, height = 5, command = Decrypt).pack(side = RIGHT)

    window.mainloop()

makeWindow()
