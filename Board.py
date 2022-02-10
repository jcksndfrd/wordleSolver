import tkinter as master
class Board:
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

    def ___init__(self):
        self.BUTTON_WIDTH = 10
        self.DEFAULT_COLOUR = "grey"
        self.button1Colour, self.button2Colour, self.button3Colour, self.button4Colour, self.button5Colour = self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR, self.DEFAULT_COLOUR

        window = master.Tk()
        window.geometry("1000x500")

        mainmenu = master.Menu()
        mainmenu.add_command(label="Reset", command=self.reset)

        label = master.Label(text="Input Letters")
        label.grid(row=0, column=2)

        entry1 = master.Entry(justify=master.CENTER)
        entry2 = master.Entry(justify=master.CENTER)
        entry3 = master.Entry(justify=master.CENTER)
        entry4 = master.Entry(justify=master.CENTER)
        entry5 = master.Entry(justify=master.CENTER)

        entry1.grid(row=1, column=0)
        entry2.grid(row=1, column=1)
        entry3.grid(row=1, column=2)
        entry4.grid(row=1, column=3)
        entry5.grid(row=1, column=4)

        button1 = master.Button(command=self.changeColourButton1, bg=self.button1Colour)
        button2 = master.Button(command=self.changeColourButton2, bg=self.button2Colour)
        button3 = master.Button(command=self.changeColourButton3, bg=self.button3Colour)
        button4 = master.Button(command=self.changeColourButton4, bg=self.button4Colour)
        button5 = master.Button(command=self.changeColourButton5, bg=self.button5Colour)

        button1.config(width=self.BUTTON_WIDTH)
        button2.config(width=self.BUTTON_WIDTH)
        button3.config(width=self.BUTTON_WIDTH)
        button4.config(width=self.BUTTON_WIDTH)
        button5.config(width=self.BUTTON_WIDTH)

        button1.grid(row=2, column=0)
        button2.grid(row=2, column=1)
        button3.grid(row=2, column=2)
        button4.grid(row=2, column=3)
        button5.grid(row=2, column=4)

        goButton = master.Button(command=self.start, bg="cyan", text="Go!")
        goButton.config(width=2*self.BUTTON_WIDTH)
        goButton.grid(row=3, column=2)

        usedLettersLabel = master.Label(text="Used Letters")
        usedLettersLabel.grid(row=4, column=1)

        usedLetters = ["a","b","c"]
        usedLettersListBox = master.Listbox()
        for item in usedLetters:
            usedLettersListBox.insert(master.END, item)
        usedLettersListBox.grid(row=5, column=1)

        usedLettersLabel = master.Label(text="Guessed Words")
        usedLettersLabel.grid(row=4, column=3)

        usedLetters = ["Queen", "Penis", "There"]
        usedLettersListBox = master.Listbox()
        for item in usedLetters:
            usedLettersListBox.insert(master.END, item)
        usedLettersListBox.grid(row=5, column=3)

        window.mainloop()
