import tkinter as tk
from tkinter import ttk
from tkinter import * 
import random
from PIL import Image
from PIL import ImageTk
import time
# this is a function to get the user input from the text input box
def getInputAmount():
	userInput = Amount.get()
	return userInput



root = Tk()

# This is the section of code which creates the main window
root.geometry('900x600')
root.configure(background='#F0F8FF')
root.title('St Petersburg Paradox')


# This is the section of code which creates the a label
Label(root, text='St Petersburg Paradox', bg='#F0F8FF', font=('arial', 30, 'bold')).place(x=280, y=30)


# This is the section of code which creates the a label
Label(root, text='Sampling Phase', bg='#F0F8FF', font=('arial', 20, 'normal')).place(x=400, y=100)


# This is the section of code which creates the a label
Label(root, text='Enter an Amount', bg='#F0F8FF', font=('arial', 18, 'normal')).place(x=100, y=200)


# This is the section of code which creates a text input box
Amount=Entry(root)
Amount.place(x=300, y=205,width=150,height=25)


#load heads
loadImage = Image.open("heads.jpg")
loadImage = loadImage.resize((150, 150))
heads = ImageTk.PhotoImage(loadImage)

#load tails
loadImage = Image.open("tails.jpg")
loadImage = loadImage.resize((150, 150))
tails = ImageTk.PhotoImage(loadImage)

# This is the section of code which creates a image
coinResult = Label(root, image=heads)
coinResult.place(x=400, y=300)


# This is the section of code which creates the a label
Label(root, text='Number of heads: ', bg='#F0F8FF', font=('arial', 18, 'normal')).place(x=500, y=200,)

# This is the section of code which creates the a label
showHeadCount = Label(root, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
showHeadCount.place(x=700, y=200, width= 70)

# This is the section of code which creates the a label
Label(root, text='Amount won: ', bg='#F0F8FF', font=('arial', 18, 'normal')).place(x=500, y=250)

# This is the section of code which creates the a label
showAmountWon = Label(root, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
showAmountWon.place(x=700, y=250, width= 70)

clicksCount = 0

def startGame():
    global clicksCount
    clicksCount+=1
    start["state"] = "disabled"
    headcount = 0
    while(True):
        outcome=random.randint(0,1)
        if outcome == 0:
            coinResult.config(image=heads)
            headcount+=1
        else:
            coinResult.config(image=tails)
            break
        showHeadCount.config(text= str(headcount))
        #showAmountWon.config(text= str(2**headcount))
    showAmountWon.config(text= str(clicksCount))
    start["state"] = "normal"

def flip():
    num = random.randint(0,1)
    if num == 0:
        coinResult.config(image=heads)
    else:
        coinResult.config(image=tails)

        
#def startGame():


start = Button(root, text="Start Game", bg='#FF7F7F', activebackground="lightgray", padx=10, pady=10, command=startGame)
start.config(font=('arial', 12, 'bold'))
start.place(x=430, y=500)

root.mainloop()
