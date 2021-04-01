#TODO: make buttons work
#TODO: in the case of no ley input, generate key
#TODO: or make no option to input key

from tkinter import *

def makeWindow():
    window = tkinter.Tk()
    window.resizable(0,0)
    window.geometry("675x350")

    buttonFrame = Frame(window).pack(side = BOTTOM)
    textFrame = Frame(window).pack(side = TOP)


    def makeButton(buttonText, buttonSide):
        button = tkinter.Button(buttonFrame, text = buttonText, width = 40, height = 5).pack(side = buttonSide)
        return button

    def makeText(fieldName, fieldHeight):
        label = tkinter.Label(textFrame, text = fieldName).pack()

        entry = tkinter.Text(height = fieldHeight).pack()
        return entry


    messageText = makeText('Message:', 7)
    keyText = makeText('Key:', 1)

    encryptButton = makeButton('Encrypt', LEFT)
    decryptButton = makeButton('Decrypt', RIGHT)

    window.mainloop()
    return messageText, keyText
