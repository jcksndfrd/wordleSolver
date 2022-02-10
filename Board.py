import tkinter as tk
from tkinter import messagebox
from Gamestate import Gamestate
from checkData import checkdataIsOneLetter

class Board:
    def __init__(self, master):
        self.game = Gamestate()
        self.master = master
        self.frame = tk.Frame(self.master)

        self.BUTTON_WIDTH = 10
        self.DEFAULT_COLOUR = "grey"
        self.button1Colour, self.button2Colour, self.button3Colour, self.button4Colour, self.button5Colour = self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR

        self.label = tk.Label(text="Input Letters")
        self.label.grid(row=0, column=2)

        self.entry1 = tk.Entry(justify=tk.CENTER)
        self.entry2 = tk.Entry(justify=tk.CENTER)
        self.entry3 = tk.Entry(justify=tk.CENTER)
        self.entry4 = tk.Entry(justify=tk.CENTER)
        self.entry5 = tk.Entry(justify=tk.CENTER)

        self.entry1.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=1, column=2)
        self.entry4.grid(row=1, column=3)
        self.entry5.grid(row=1, column=4)

        self.button1 = tk.Button(command=self.changeColourButton1, bg=self.button1Colour)
        self.button2 = tk.Button(command=self.changeColourButton2, bg=self.button2Colour)
        self.button3 = tk.Button(command=self.changeColourButton3, bg=self.button3Colour)
        self.button4 = tk.Button(command=self.changeColourButton4, bg=self.button4Colour)
        self.button5 = tk.Button(command=self.changeColourButton5, bg=self.button5Colour)

        self.button1.config(width=self.BUTTON_WIDTH)
        self.button2.config(width=self.BUTTON_WIDTH)
        self.button3.config(width=self.BUTTON_WIDTH)
        self.button4.config(width=self.BUTTON_WIDTH)
        self.button5.config(width=self.BUTTON_WIDTH)

        self.button1.grid(row=2, column=0)
        self.button2.grid(row=2, column=1)
        self.button3.grid(row=2, column=2)
        self.button4.grid(row=2, column=3)
        self.button5.grid(row=2, column=4)

        self.goButton = tk.Button(command=self.start, bg="cyan", text="Go!")
        self.goButton.config(width=2*self.BUTTON_WIDTH)
        self.goButton.grid(row=3, column=2)

        self.usedLettersLabel = tk.Label(text="Used Letters")
        self.usedLettersLabel.grid(row=4, column=1)

        self.usedLetters = []
        self.usedLettersListBox = tk.Listbox()

        self.topWordsLabel = tk.Label(text="Top Words")
        self.topWordsLabel.grid(row=4, column=2)

        self.topWords = self.game.topWords(5)
        self.topWordsListBox = tk.Listbox()

        self.usedWordsLabel = tk.Label(text="Guessed Words")
        self.usedWordsLabel.grid(row=4, column=3)

        self.usedWords = []
        self.usedWordsListBox = tk.Listbox()
        self.setListBoxes()

        self.menubar = tk.Menu(self.master)
        self.menubar.add_command(label="Exit", command=self.master.quit)
        self.menubar.add_command(label="Use top word", command=self.useTopWord)
        self.menubar.add_command(label="Reset", command=self.reset)
        self.master.config(menu=self.menubar)

    def setListBoxes(self):
        self.usedLettersListBox.delete(0, tk.END)
        for item in self.usedLetters:
            self.usedLettersListBox.insert(tk.END, item)
        self.usedLettersListBox.grid(row=5, column=1)
        
        self.topWordsListBox.delete(0, tk.END)
        for item in self.topWords:
            self.topWordsListBox.insert(tk.END, item)
        self.topWordsListBox.grid(row=5, column=2)

        self.usedWordsListBox.delete(0, tk.END)
        for item in self.usedWords:
            self.usedWordsListBox.insert(tk.END, item)
        self.usedWordsListBox.grid(row=5, column=3)

    def changeColourButton1(self):
        if self.button1Colour == "grey":
            self.button1Colour = "green"
            self.button1.configure(bg=self.button1Colour)
        elif self.button1Colour == "green":
            self.button1Colour = "orange"
            self.button1.configure(bg=self.button1Colour)
        elif self.button1Colour == "orange":
            self.button1Colour = "grey"
            self.button1.configure(bg=self.button1Colour)

    def changeColourButton2(self):
        if self.button2Colour == "grey":
            self.button2Colour = "green"
            self.button2.configure(bg=self.button2Colour)
        elif self.button2Colour == "green":
            self.button2Colour = "orange"
            self.button2.configure(bg=self.button2Colour)
        elif self.button2Colour == "orange":
            self.button2Colour = "grey"
            self.button2.configure(bg=self.button2Colour)

    def changeColourButton3(self):
        if self.button3Colour == "grey":
            self.button3Colour = "green"
            self.button3.configure(bg=self.button3Colour)
        elif self.button3Colour == "green":
            self.button3Colour = "orange"
            self.button3.configure(bg=self.button3Colour)
        elif self.button3Colour == "orange":
            self.button3Colour = "grey"
            self.button3.configure(bg=self.button3Colour)
            
    def changeColourButton4(self):
        if self.button4Colour == "grey":
            self.button4Colour = "green"
            self.button4.configure(bg=self.button4Colour)
        elif self.button4Colour == "green":
            self.button4Colour = "orange"
            self.button4.configure(bg=self.button4Colour)
        elif self.button4Colour == "orange":
            self.button4Colour = "grey"
            self.button4.configure(bg=self.button4Colour)
            
    def changeColourButton5(self):
        if self.button5Colour == "grey":
            self.button5Colour = "green"
            self.button5.configure(bg=self.button5Colour)
        elif self.button5Colour == "green":
            self.button5Colour = "orange"
            self.button5.configure(bg=self.button5Colour)
        elif self.button5Colour == "orange":
            self.button5Colour = "grey"
            self.button5.configure(bg=self.button5Colour)

    def getNumberFromString(self, text):
        if text == "grey":
            return 0
        elif text == "green":
            return 1
        elif text == "orange":
            return 2

    def getNumbersFromButtons(self):
        return [self.getNumberFromString(self.button1Colour), self.getNumberFromString(self.button2Colour), self.getNumberFromString(self.button3Colour), self.getNumberFromString(self.button4Colour), self.getNumberFromString(self.button5Colour)]
    
    def reset(self):
        self.game.reset()
        self.topWords = self.game.topWords(5)
        self.usedWords = []
        self.usedLetters = []
        self.clearEntries()
        self.setListBoxes()
        self.resetButtons()

    def resetButtons(self):
        self.button1Colour = "grey"
        self.button2Colour = "grey"
        self.button3Colour = "grey"
        self.button4Colour = "grey"
        self.button5Colour = "grey"
        self.button1.configure(bg=self.button1Colour)
        self.button2.configure(bg=self.button2Colour)
        self.button3.configure(bg=self.button3Colour)
        self.button4.configure(bg=self.button4Colour)
        self.button5.configure(bg=self.button5Colour)


    def clearEntries(self):
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry4.delete(0, "end")
        self.entry5.delete(0, "end")

    def useTopWord(self):
        self.clearEntries()
        self.entry1.insert(0, self.topWords[0][0])
        self.entry2.insert(0, self.topWords[0][1])
        self.entry3.insert(0, self.topWords[0][2])
        self.entry4.insert(0, self.topWords[0][3])
        self.entry5.insert(0, self.topWords[0][4])

    def start(self):
        letters = [self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get()]
        word = "".join(letters)

        doGame = True
        for _, item in enumerate(letters):
            if not checkdataIsOneLetter(item):
                doGame = False

        numbers = self.getNumbersFromButtons()

        win = True
        for n in numbers:
            if n != 1:
                win = False
        
        if win:
            doGame = False
            messagebox.showinfo(title="You Win!", message="Congradulations! You are a winner!")
            self.reset()

        if doGame:
            
            self.game.filterWords(word, numbers)
        
            for i, l in enumerate(letters):
                if numbers[i] == 0:
                    if l not in self.usedLetters:
                        self.usedLetters.append(l)
            self.usedWords.append(word)
            self.topWords = self.game.topWords(5)
            self.setListBoxes()
            self.clearEntries()
            self.resetButtons()
        elif not doGame and not win:
            messagebox.showerror(title="Incorrect Data", message="Must input letters of one space.")