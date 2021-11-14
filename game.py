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
        tk.Label(self.frame, text='St Petersburg Paradox', bg='#F0F8FF', font=('arial', 30, 'bold')).grid(pady=3,row=0,rowspan=2,column=0,columnspan=6)
    


        # This is the section of code which creates the label to show which phase
        tk.Label(self.frame, text='Sampling Phase', bg='#F0F8FF', font=('arial', 20, 'normal')).grid(pady=3,row=2,column=0,columnspan=6)


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
        coinResult.grid(pady=3,row=6,column=2,columnspan=2,rowspan=2)

        # This is the section of code which creates the a label for flipcount
        tk.Label(self.frame, text='Flip Count: ', bg='#F0F8FF', font=('arial', 18, 'normal')).grid(pady=3,row=8,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates the a label to diplay flipcount variable
        self.showFlipCount = tk.Label(self.frame, text='0', bg='#F0F8FF', font=('arial', 18, 'normal'))
        self.showFlipCount.grid(pady=3,row=8,column=3,columnspan=3,padx=10,sticky=W)


        # This is the section of code which creates the a label for headscount
        tk.Label(self.frame, text='Number of heads: ', bg='#F0F8FF', font=('arial', 18, 'normal')).grid(pady=3,row=9,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates the a label for headcount variable
        self.showHeadCount = tk.Label(self.frame, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
        self.showHeadCount.grid(pady=3,row=9,column=3,columnspan=3,padx=10,sticky=W)


        # This is the section of code which creates the a label for amount won
        tk.Label(self.frame, text='Amount won: ', bg='#F0F8FF', font=('arial', 18, 'normal')).grid(pady=3,row=10,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates the a label to display amount won variable
        self.showAmountWon = tk.Label(self.frame, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
        self.showAmountWon.grid(pady=3,row=10,column=3,columnspan=3,padx=10,sticky=W)
        
        # This is the section of code which creates the a label for entry amount
        tk.Label(self.frame, text='Enter an Amount', bg='#F0F8FF', font=('arial', 18, 'normal')).grid(pady=3,row=11,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates a text input box to enter amount
        self.Amount=Entry(self.frame)
        self.Amount.grid(row=11,column=3,columnspan=3,sticky=W,padx=10,ipadx=5,ipady=3,pady=5)

        # This is the section of code which creates the a label for invalid entry
        self.invalidAmount = tk.Label(self.frame, text='',fg='red', font=('arial', 12, 'normal'))
        self.invalidAmount.grid(row=12,column=0,columnspan=6)

        #clicksCount=0
        #simulates game phase
        def startGame():
            #global clicksCount
            #clicksCount+=1
            
            #intialize variables to display
            headcount = 0               
            flips=0
            amountWon=0
            #reset count and amount won to 0
            self.showFlipCount.config(text= str(0))
            self.showHeadCount.config(text= str(0)) 
            self.showAmountWon.config(text= str(0))
            
            #update window and sleep
            root.update()
            time.sleep(1)


            while(True):

                #increment flip count and update text window
                flips+=1
                self.showFlipCount.config(text= str(flips))

                #simulate head or tails and update variables
                outcome=random.randint(0,1)
                if outcome == 0:
                    coinResult.config(image=heads)
                    headcount+=1
                    amountWon=2**(flips)
                    root.update()
                else:
                    coinResult.config(image=tails)
                    amountWon=2**(flips)
                    self.showHeadCount.config(text= str(headcount))
                    self.showAmountWon.config(text= str(amountWon))
                    root.update()
                    break

                #update labels and window and sleep for showing result
                self.showHeadCount.config(text= str(headcount))
                self.showAmountWon.config(text= str(amountWon))
                root.update()
                time.sleep(1)
            #another sleep after break statement    
            time.sleep(1)

            #rest flip count and slip outcomes to 0 and unknown
            #self.showFlipCount.config(text= str(0))
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
                self.invalidAmount.config(text= "Enter a valid positive Integer")
                self.Amount.delete(0, 'end')
                print("not a valid integer")
            else:
                #check if input amount is more than 0
                if(int(amountBet)>0):
                    self.invalidAmount.config(text= "")
                    startGame()
                else:
                    self.Amount.delete(0, 'end')
                    self.invalidAmount.config(text= "Enter a valid postive Integer only")

            #enable startgame button
            start["state"] = "normal"
        


        # This is the section of code which creates a button to start one cycle of coin flip simulation
        start = tk.Button(self.frame, text="Start Game", bg='#FF7F7F', activebackground="lightgray", padx=10, pady=10, command=validate)
        start.config(font=('arial', 12, 'bold'))
        start.grid(row=13,column=2,columnspan=2,padx=10,pady=10)

        # This is the section of code which creates a button to switch to decision phase
        tk.Button(self.frame, text='Go to Decision Phase', bg='#7ee643', activebackground="lightgray",font=('arial', 12,'bold'), command=self.make_page_1).grid(row=14,column=1,columnspan=4,padx=10,pady=10)

        #assign context variable for decision page
        self.page_1 = Page_1(master=self.root, app=self)

        self.frame.mainloop()


    #loads the current frame when switching
    def main_page(self):
        self.frame.pack()

    #forgets current page and calls loading function for decision frame
    def make_page_1(self):

        #resets entry and error
        self.invalidAmount.config(text= "")
        self.Amount.delete(0, 'end')
        self.showFlipCount.config(text= str(0))
        self.showHeadCount.config(text= str(0)) 
        self.showAmountWon.config(text= str(0))


        self.frame.pack_forget()
        self.page_1.start_page()


class Page_1:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        #root.geometry('900x600')

        
        # This is the section of code which creates the heading label
        tk.Label(self.frame, text='St Petersburg Paradox', bg='#F0F8FF', font=('arial', 30, 'bold')).grid(pady=3,row=0,rowspan=2,column=0,columnspan=6)
    


        # This is the section of code which creates the label to show which phase
        tk.Label(self.frame, text='Decision Phase', bg='#F0F8FF', font=('arial', 20, 'normal')).grid(pady=3,row=2,column=0,columnspan=6)


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
        coinResult.grid(pady=3,row=6,column=2,columnspan=2,rowspan=2)

        # This is the section of code which creates the a label for flipcount
        tk.Label(self.frame, text='Flip Count: ', bg='#F0F8FF', font=('arial', 18, 'normal')).grid(pady=3,row=8,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates the a label to diplay flipcount variable
        showFlipCount = tk.Label(self.frame, text='0', bg='#F0F8FF', font=('arial', 18, 'normal'))
        showFlipCount.grid(pady=3,row=8,column=3,columnspan=3,padx=10,sticky=W)


        # This is the section of code which creates the a label for headscount
        tk.Label(self.frame, text='Number of heads: ', bg='#F0F8FF', font=('arial', 18, 'normal')).grid(pady=3,row=9,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates the a label for headcount variable
        showHeadCount = tk.Label(self.frame, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
        showHeadCount.grid(pady=3,row=9,column=3,columnspan=3,padx=10,sticky=W)


        # This is the section of code which creates the a label for amount won
        tk.Label(self.frame, text='Amount won: ', bg='#F0F8FF', font=('arial', 18, 'normal')).grid(pady=3,row=10,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates the a label to display amount won variable
        showAmountWon = tk.Label(self.frame, text='0', bg='#ADD8E6', font=('arial', 18, 'normal'))
        showAmountWon.grid(pady=3,row=10,column=3,columnspan=3,padx=10,sticky=W)
        
        # This is the section of code which creates the a label for entry amount
        tk.Label(self.frame, text='Enter an Amount', bg='#F0F8FF', font=('arial', 18, 'normal')).grid(pady=3,row=11,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates a text input box to enter amount
        self.Amount=Entry(self.frame)
        self.Amount.grid(row=11,column=3,columnspan=3,sticky=W,padx=10,ipadx=5,ipady=3,pady=5)

        # This is the section of code which creates the a label for invalid entry
        self.invalidAmount = tk.Label(self.frame, text='',fg='red', font=('arial', 12, 'normal'))
        self.invalidAmount.grid(row=12,column=0,columnspan=6)


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
                    amountWon=2**flips
                    root.update()
                else:
                    coinResult.config(image=tails)
                    amountWon=2**(flips)
                    showHeadCount.config(text= str(headcount))
                    showAmountWon.config(text= str(amountWon))
                    root.update()
                    break

                #update labels and window and sleep for showing result
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
                self.invalidAmount.config(text= "Enter a valid postive Integer only")
                self.Amount.delete(0, 'end')
                print("not a valid integer")
            else:
                #check if input amount is more than 0
                if(int(amountBet)>=0):
                    self.invalidAmount.config(text= "")
                    startGame()
                else:
                    self.invalidAmount.config(text= "Enter a valid postive Integer only")
                    self.Amount.delete(0, 'end')
                    print(" only positive number allowed")

            #enable startgame button
            start["state"] = "normal"

        # This is the section of code which creates a button to start one cycle of coin flip simulation
        start = tk.Button(self.frame, text="Start Game", bg='#FF7F7F', activebackground="lightgray", padx=10, pady=10, command=validate)
        start.config(font=('arial', 12, 'bold'))
        start.grid(row=13,column=2,columnspan=2,padx=10,pady=10)
        
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
        tk.Label(self.frame, text='St Petersburg Paradox', bg='#F0F8FF', font=('arial', 30, 'bold')).grid(pady=3,row=0,rowspan=2,column=0,columnspan=6)

        # This is the section of code which creates the a label for heading
        tk.Label(self.frame, text='Outcome', bg='#F0F8FF', font=('arial', 20, 'normal')).grid(pady=3,row=2,column=0,columnspan=6)

        # This is the section of code which creates amount bet label
        tk.Label(self.frame, text='Amount Bet:', font=('arial', 18, 'normal')).grid(pady=3,row=5,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates the a label to display amount bet variable
        AmountBetLabel = tk.Label(self.frame, text=str(amountBet), font=('arial', 18, 'normal'))
        AmountBetLabel.grid(pady=3,row=5,column=3,columnspan=3,padx=10,sticky=W)

        # This is the section of code which creates the a label text for amount won
        tk.Label(self.frame, text='Amount Won:', font=('arial', 18, 'normal')).grid(pady=3,row=6,column=0,columnspan=3,sticky=E)

        # This is the section of code which creates the a label to display amount won variable
        AmountWonLabel = tk.Label(self.frame, text=str(amountWon), font=('arial', 18, 'normal'))
        AmountWonLabel.grid(pady=3,row=6,column=3,columnspan=3,padx=10,sticky=W)

        # This is the section of code which creates a button to switch to Sampling phase
        tk.Button(self.frame, text='Go back to Sampling Phase', bg='#7ee643', activebackground="lightgray",font=('arial', 12,'bold'), command=self.go_back).grid(row=8,column=1,columnspan=4,padx=10,pady=10)

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
