import tkinter as tk
from tkinter import ttk
from tkinter import * 
import random
from PIL import Image
from PIL import ImageTk
import time


class App:

    def __init__(self, root=None):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        self.root.geometry('900x600')
        self.root.configure(background='#F0F8FF')
        self.root.title('St Petersburg Paradox')


        # This is the section of code which creates the heading label
        tk.Label(self.frame, text='St Petersburg Paradox', bg='#F0F8FF', font=('arial', 30, 'bold')).pack()
    


        # This is the section of code which creates the label to show which phase
        tk.Label(self.frame, text='Sampling Phase', bg='#F0F8FF', font=('arial', 20, 'normal')).pack()


        #load heads to display later
        loadImage = Image.open("heads.jpg")
        loadImage = loadImage.resize((150, 150))
        heads = ImageTk.PhotoImage(loadImage)

        #load tails to display later
        load = Image.open("tails.jpg")
        load = load.resize((150, 150))
        tails = ImageTk.PhotoImage(load)

        #load unknown to display later
        load2 = Image.open("unknown.jpg")
        load2 = load2.resize((150, 150))
        unknown = ImageTk.PhotoImage(load2)

        # This is the section of code which creates a image to show coin flip output
        coinResult = tk.Label(self.frame, image=unknown)
        coinResult.pack()

        # This is the section of code which creates the a label for flipcount
        tk.Label(self.frame, text='Flip Count: ', bg='#F0F8FF', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates the a label to diplay flipcount variable
        showFlipCount = tk.Label(self.frame, text='0', bg='#F0F8FF', font=('arial', 18, 'normal'))
        showFlipCount.pack()


        # This is the section of code which creates the a label for headscount
        tk.Label(self.frame, text='Number of heads: ', bg='#F0F8FF', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates the a label for headcount variable
        showHeadCount = tk.Label(self.frame, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
        showHeadCount.pack()


        # This is the section of code which creates the a label for amount won
        tk.Label(self.frame, text='Amount won: ', bg='#F0F8FF', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates the a label to display amount won variable
        showAmountWon = tk.Label(self.frame, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
        showAmountWon.pack()
        
        # This is the section of code which creates the a label for entry amount
        tk.Label(self.frame, text='Enter an Amount', bg='#F0F8FF', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates a text input box to enter amount
        self.Amount=Entry(self.frame)
        self.Amount.pack()

        # This is the section of code which creates the a label for invalid entry
        invalidAmount = tk.Label(self.frame, text='',fg='red', font=('arial', 12, 'normal'))
        invalidAmount.pack()

        #clicksCount=0
        #simulates game phase
        def startGame():
            #global clicksCount
            #clicksCount+=1
            
            #intialize variables to display
            headcount = 0               
            flips=0

            #reset count and amount won to 0
            showHeadCount.config(text= str(headcount)) 
            showAmountWon.config(text= str(headcount))
            
            #update window and sleep
            root.update()
            time.sleep(1)


            while(True):

                #increment flip count and update text window
                flips+=1
                showFlipCount.config(text= str(flips))

                #simulate head or tails and update variables
                outcome=random.randint(0,1)
                if outcome == 0:
                    coinResult.config(image=heads)
                    headcount+=1
                    root.update()
                else:
                    coinResult.config(image=tails)
                    root.update()
                    break

                #update labels and window and sleep for showing result
                showHeadCount.config(text= str(headcount))
                showAmountWon.config(text= str(2**headcount))
                root.update()
                time.sleep(1)
            #another sleep after break statement    
            time.sleep(1)

            #rest flip count and slip outcomes to 0 and unknown
            showFlipCount.config(text= str(0))
            coinResult.config(image=unknown)
            self.Amount.delete(0, 'end')
            root.update()
            
            

        #validate valid input in amount text
        def validate():
            #disables start button while simulation is on
            start["state"] = "disabled"  
            #fetch input text
            amountBet=self.Amount.get()
            
            #check if input is integer
            try:
                integer_result = int(amountBet)
            except ValueError:
                invalidAmount.config(text= "Enter a valid positive Integer")
                print("not a valid integer")
            else:
                #check if input amount is more than 0
                if(int(amountBet)>0):
                    invalidAmount.config(text= "")
                    startGame()
                else:
                    invalidAmount.config(text= "Enter a valid postive Integer only")

            #enable startgame button
            start["state"] = "normal"
        


        # This is the section of code which creates a button to start one cycle of coin flip simulation
        start = tk.Button(self.frame, text="Start Game", bg='#FF7F7F', activebackground="lightgray", padx=10, pady=10, command=validate)
        start.config(font=('arial', 12, 'bold'))
        start.pack()

        # This is the section of code which creates a button to switch to decision phase
        tk.Button(self.frame, text='Go to Decision Phase', command=self.make_page_1).pack()

        #assign context variable for decision page
        self.page_1 = Page_1(master=self.root, app=self)

        self.frame.mainloop()


    #loads the current frame when switching
    def main_page(self):
        self.frame.pack()

    #forgets current page and calls loading function for decision frame
    def make_page_1(self):
        self.frame.pack_forget()
        self.page_1.start_page()


class Page_1:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        #root.geometry('900x600')

        
        # This is the section of code which creates the heading label
        tk.Label(self.frame, text='St Petersburg Paradox', bg='#F0F8FF', font=('arial', 30, 'bold')).pack()
    


        # This is the section of code which creates the label to show which phase
        tk.Label(self.frame, text='Sampling Phase', bg='#F0F8FF', font=('arial', 20, 'normal')).pack()


        #load heads to display later
        loadImage = Image.open("heads.jpg")
        loadImage = loadImage.resize((150, 150))
        heads = ImageTk.PhotoImage(loadImage)

        #load tails to display later
        load = Image.open("tails.jpg")
        load = load.resize((150, 150))
        tails = ImageTk.PhotoImage(load)

        #load unknown to display later
        load2 = Image.open("unknown.jpg")
        load2 = load2.resize((150, 150))
        unknown = ImageTk.PhotoImage(load2)

        # This is the section of code which creates a image to show coin flip output
        coinResult = tk.Label(self.frame, image=unknown)
        coinResult.pack()

        # This is the section of code which creates the a label for flipcount
        tk.Label(self.frame, text='Flip Count: ', bg='#F0F8FF', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates the a label to diplay flipcount variable
        showFlipCount = tk.Label(self.frame, text='0', bg='#F0F8FF', font=('arial', 18, 'normal'))
        showFlipCount.pack()


        # This is the section of code which creates the a label for headscount
        tk.Label(self.frame, text='Number of heads: ', bg='#F0F8FF', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates the a label for headcount variable
        showHeadCount = tk.Label(self.frame, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
        showHeadCount.pack()


        # This is the section of code which creates the a label for amount won
        tk.Label(self.frame, text='Amount won: ', bg='#F0F8FF', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates the a label to display amount won variable
        showAmountWon = tk.Label(self.frame, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
        showAmountWon.pack()

        # This is the section of code which creates the a label for entry amount
        tk.Label(self.frame, text='Enter an Amount', bg='#F0F8FF', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates a text input box to enter amount
        self.Amount=Entry(self.frame)
        self.Amount.pack()

        # This is the section of code which creates the a label for invalid entry
        invalidAmount = tk.Label(self.frame, text='',fg='red', font=('arial', 12, 'normal'))
        invalidAmount.pack()


        #clicksCount = 0
        def startGame():
            #global clicksCount
            #clicksCount+=1
            
            #intialize variables to display
            headcount = 0               
            flips=0
            amountWon=0
            #reset count and amount won to 0
            showHeadCount.config(text= str(headcount)) 
            showAmountWon.config(text= str(headcount))
            
            #update window and sleep
            root.update()
            time.sleep(1)


            while(True):

                #increment flip count and update text window
                flips+=1
                showFlipCount.config(text= str(flips))

                #simulate head or tails and update variables
                outcome=random.randint(0,1)
                if outcome == 0:
                    coinResult.config(image=heads)
                    headcount+=1
                    root.update()
                else:
                    coinResult.config(image=tails)
                    root.update()
                    break

                #update labels and window and sleep for showing result
                amountWon=2**headcount
                showHeadCount.config(text= str(headcount))
                showAmountWon.config(text= str(amountWon))
                root.update()
                time.sleep(1)
            #another sleep after break statement    
            time.sleep(2)

            #rest flip count and slip outcomes to 0 and unknown
            showFlipCount.config(text= str(0))
            coinResult.config(image=unknown)
            root.update()

            #reset flip result to 0
            showHeadCount.config(text= str(0))
            showAmountWon.config(text= str(0))

            #loads the result page and pass the outcomes to the page
            self.page_2 = Page_2(master=master, app=app, amountBet=self.Amount.get(),amountWon=amountWon)
            self.Amount.delete(0, 'end')
            #switch to result page
            self.make_page_2()
            

        #validate valid input in amount text
        def validate():
            #disables start button while simulation is on
            start["state"] = "disabled"  
            #fetch input text
            amountBet=self.Amount.get()
            
            #check if input is integer
            try:
                integer_result = int(amountBet)
            except ValueError:
                invalidAmount.config(text= "Enter a valid postive Integer only")
                print("not a valid integer")
            else:
                #check if input amount is more than 0
                if(int(amountBet)>=0):
                    invalidAmount.config(text= "")
                    startGame()
                else:
                    invalidAmount.config(text= "Enter a valid postive Integer only")
                    print(" only positive number allowed")

            #enable startgame button
            start["state"] = "normal"

        # This is the section of code which creates a button to start one cycle of coin flip simulation
        start = tk.Button(self.frame, text="Start Game", bg='#FF7F7F', activebackground="lightgray", padx=10, pady=10, command=validate)
        start.config(font=('arial', 12, 'bold'))
        start.pack()
        
        #tk.Label(self.frame, text='Page 1').pack()
        #tk.Button(self.frame, text='Go back', command=self.make_page_2).pack()

        #assign context variable for result frame
        self.page_2 = Page_2(master=master, app=app)

    #loads the current frame when switching
    def start_page(self):
        self.frame.pack()

    #forgets current page and calls loading function for result frame
    def make_page_2(self):
        self.frame.pack_forget()
        self.page_2.start_page()

class Page_2:
    def __init__(self, master=None, app=None, amountBet=0, amountWon=0):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)


        # This is the section of code which creates the heading label
        tk.Label(self.frame, text='St Petersburg Paradox', bg='#F0F8FF', font=('arial', 30, 'bold')).pack()

        # This is the section of code which creates the a label for heading
        tk.Label(self.frame, text='Outcome').pack()

        # This is the section of code which creates amount bet label
        tk.Label(self.frame, text='Amount Bet:', bg='#ADD8E6', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates the a label to display amount bet variable
        AmountBetLabel = tk.Label(self.frame, text=str(amountBet), bg='#ADD8E6', font=('arial', 18, 'normal'))
        AmountBetLabel.pack()

        # This is the section of code which creates the a label text for amount won
        tk.Label(self.frame, text='Amount Won:', bg='#ADD8E6', font=('arial', 18, 'normal')).pack()

        # This is the section of code which creates the a label to display amount won variable
        AmountWonLabel = tk.Label(self.frame, text=str(amountWon), bg='#ADD8E6', font=('arial', 18, 'normal'))
        AmountWonLabel.pack()

        # This is the section of code which creates a button to switch to decision phase
        tk.Button(self.frame, text='Go back to Sampling Phase', command=self.go_back).pack()

    #loads the current frame when switching
    def start_page(self):
        self.frame.pack()

    #forgets current page and calls loading function for result frame
    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
