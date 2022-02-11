import tkinter as tk
from tkinter import messagebox
from Gamestate import Gamestate
import JamesLib as extras

class Board:
    def __init__(self, master):
        self.game = Gamestate()
        self.master = master
        self.frame = tk.Frame(self.master)

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

        self.colourBlindMode = True
        self.BUTTON_WIDTH = 10
        self.setColourBlind()
        self.button1Colour, self.button2Colour, self.button3Colour, self.button4Colour, self.button5Colour = self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR

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
        self.menubar.add_command(label="Colourblind Mode", command=self.setColourBlind)

        self.algorithmMenu = tk.Menu(self.menubar, tearoff=False)
        self.algorithmMenu.add_command(label="Jacks", command=self.jacksAlogirthm)
        self.algorithmMenu.add_command(label="James'", command=self.jamesAlgorithm)
        self.menubar.add_cascade(label="Choose Algorithm", menu=self.algorithmMenu)
        self.master.config(menu=self.menubar)

        self.currentAlgorithmLabel = tk.Label(text="Current Algorithm:")
        self.currentAlgorithmLabel.grid(row=6, column=3)
        self.whoseAlgorithmLabel = tk.Label(text="Jacks")
        self.whoseAlgorithmLabel.grid(row=6, column=4)

    def jacksAlogirthm(self):
        self.reset()
        self.game = Gamestate()
        self.whoseAlgorithmLabel.configure(text="Jacks")

    def jamesAlgorithm(self):
        self.reset()
        self.game = Gamestate()
        self.whoseAlgorithmLabel.configure(text="James'")

    def setColourBlind(self):
        self.colourBlindMode = not self.colourBlindMode
        if self.colourBlindMode:
            self.DEFAULT_COLOUR = "grey"
            self.PRIMARY_COLOUR = "blue"
            self.SECONDARY_COLOUR = "yellow"
        else:
            self.DEFAULT_COLOUR = "grey"
            self.PRIMARY_COLOUR = "green"
            self.SECONDARY_COLOUR = "orange"

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
        if self.button1Colour == self.DEFAULT_COLOUR:
            self.button1Colour = self.PRIMARY_COLOUR
            self.button1.configure(bg=self.button1Colour)
        elif self.button1Colour == self.PRIMARY_COLOUR:
            self.button1Colour = self.SECONDARY_COLOUR
            self.button1.configure(bg=self.button1Colour)
        elif self.button1Colour == self.SECONDARY_COLOUR:
            self.button1Colour = self.DEFAULT_COLOUR
            self.button1.configure(bg=self.button1Colour)

    def changeColourButton2(self):
        if self.button2Colour == self.DEFAULT_COLOUR:
            self.button2Colour = self.PRIMARY_COLOUR
            self.button2.configure(bg=self.button2Colour)
        elif self.button2Colour == self.PRIMARY_COLOUR:
            self.button2Colour = self.SECONDARY_COLOUR
            self.button2.configure(bg=self.button2Colour)
        elif self.button2Colour == self.SECONDARY_COLOUR:
            self.button2Colour = self.DEFAULT_COLOUR
            self.button2.configure(bg=self.button2Colour)

    def changeColourButton3(self):
        if self.button3Colour == self.DEFAULT_COLOUR:
            self.button3Colour = self.PRIMARY_COLOUR
            self.button3.configure(bg=self.button3Colour)
        elif self.button3Colour == self.PRIMARY_COLOUR:
            self.button3Colour = self.SECONDARY_COLOUR
            self.button3.configure(bg=self.button3Colour)
        elif self.button3Colour == self.SECONDARY_COLOUR:
            self.button3Colour = self.DEFAULT_COLOUR
            self.button3.configure(bg=self.button3Colour)
            
    def changeColourButton4(self):
        if self.button4Colour == self.DEFAULT_COLOUR:
            self.button4Colour = self.PRIMARY_COLOUR
            self.button4.configure(bg=self.button4Colour)
        elif self.button4Colour == self.PRIMARY_COLOUR:
            self.button4Colour = self.SECONDARY_COLOUR
            self.button4.configure(bg=self.button4Colour)
        elif self.button4Colour == self.SECONDARY_COLOUR:
            self.button4Colour = self.DEFAULT_COLOUR
            self.button4.configure(bg=self.button4Colour)
            
    def changeColourButton5(self):
        if self.button5Colour == self.DEFAULT_COLOUR:
            self.button5Colour = self.PRIMARY_COLOUR
            self.button5.configure(bg=self.button5Colour)
        elif self.button5Colour == self.PRIMARY_COLOUR:
            self.button5Colour = self.SECONDARY_COLOUR
            self.button5.configure(bg=self.button5Colour)
        elif self.button5Colour == self.SECONDARY_COLOUR:
            self.button5Colour = self.DEFAULT_COLOUR
            self.button5.configure(bg=self.button5Colour)

    def getNumberFromString(self, text):
        if text == self.DEFAULT_COLOUR:
            return 0
        elif text == self.PRIMARY_COLOUR:
            return 1
        elif text == self.SECONDARY_COLOUR:
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
        self.button1Colour = self.DEFAULT_COLOUR
        self.button2Colour = self.DEFAULT_COLOUR
        self.button3Colour = self.DEFAULT_COLOUR
        self.button4Colour = self.DEFAULT_COLOUR
        self.button5Colour = self.DEFAULT_COLOUR
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
            if not extras.checkdataIsOneLetter(item):
                doGame = False

        numbers = self.getNumbersFromButtons()
        win = extras.checkArrayElementsAreEqualToVar(numbers, 1)
        
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