from tkinter import *
from encyptAndDecrypt import Message
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def makeWindow():
    window = Tk()
    window.resizable(0,0)
    window.geometry("675x350")

    def Encrypt():

        key = keyText.get(1.0, 'end').strip()
        message = messageText.get(1.0, 'end').strip()

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

    def Decrypt():
        key = keyText.get(1.0, 'end').strip()
        message = messageText.get(1.0, 'end').strip()

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

    buttonFrame = Frame(window).pack(side = BOTTOM)
    inputFrame = Frame(window).pack(side = TOP)

    messageTextLabel = Label(inputFrame, text = 'Your message:').pack()
    messageText = Text(height = 7)
    messageText.pack()

    keyTextLabel = Label(inputFrame, text = 'Your Key:').pack()
    keyText = Text(height = 2)
    keyText.pack()

    encryptButton = Button(buttonFrame, text = 'Encrypt', width = 40, height = 5, command = Encrypt).pack(side = LEFT)
    decryptButton = Button(buttonFrame, text = 'Decrypt', width = 40, height = 5, command = Decrypt).pack(side = RIGHT)

    window.mainloop()

makeWindow()
