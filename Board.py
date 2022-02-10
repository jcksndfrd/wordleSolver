import tkinter as tk
class Board:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.BUTTON_WIDTH = 10
        self.DEFAULT_COLOUR = "grey"
        self.button1Colour, self.button2Colour, self.button3Colour, self.button4Colour, self.button5Colour = self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR

        self.mainmenu = tk.Menu()
        self.mainmenu.add_command(label="Reset", command=self.reset)

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

        self.usedLetters = ["a","b","c"]
        self.usedLettersListBox = tk.Listbox()
        for item in self.usedLetters:
            self.usedLettersListBox.insert(tk.END, item)
        self.usedLettersListBox.grid(row=5, column=1)

        self.usedLettersLabel = tk.Label(text="Guessed Words")
        self.usedLettersLabel.grid(row=4, column=3)

        self.usedLetters = ["Queen", "Penis", "There"]
        self.usedLettersListBox = tk.Listbox()
        for item in self.usedLetters:
            self.usedLettersListBox.insert(tk.END, item)
        self.usedLettersListBox.grid(row=5, column=3)

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

    def reset(self):
        print("reseted")
        return

    def start(self):
        print("started")
        return