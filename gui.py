import tkinter as master

def changeColourButton1():
    global button1Colour
    if button1Colour == "grey":
        button1Colour = "green"
        button1.configure(bg=button1Colour)
    elif button1Colour == "green":
        button1Colour = "orange"
        button1.configure(bg=button1Colour)
    elif button1Colour == "orange":
        button1Colour = "grey"
        button1.configure(bg=button1Colour)

def changeColourButton2():
    global button2Colour
    if button2Colour == "grey":
        button2Colour = "green"
        button2.configure(bg=button2Colour)
    elif button2Colour == "green":
        button2Colour = "orange"
        button2.configure(bg=button2Colour)
    elif button2Colour == "orange":
        button2Colour = "grey"
        button2.configure(bg=button2Colour)

def changeColourButton3():
    global button3Colour
    if button3Colour == "grey":
        button3Colour = "green"
        button3.configure(bg=button3Colour)
    elif button3Colour == "green":
        button3Colour = "orange"
        button3.configure(bg=button3Colour)
    elif button3Colour == "orange":
        button3Colour = "grey"
        button3.configure(bg=button3Colour)
        
def changeColourButton4():
    global button4Colour
    if button4Colour == "grey":
        button4Colour = "green"
        button4.configure(bg=button4Colour)
    elif button4Colour == "green":
        button4Colour = "orange"
        button4.configure(bg=button4Colour)
    elif button4Colour == "orange":
        button4Colour = "grey"
        button4.configure(bg=button4Colour)
        
def changeColourButton5():
    global button5Colour
    if button5Colour == "grey":
        button5Colour = "green"
        button5.configure(bg=button5Colour)
    elif button5Colour == "green":
        button5Colour = "orange"
        button5.configure(bg=button5Colour)
    elif button5Colour == "orange":
        button5Colour = "grey"
        button5.configure(bg=button5Colour)

def reset():
    print("reseted")
    return

def start():
    print("started")
    return

BUTTON_WIDTH = 10
DEFAULT_COLOUR = "grey"
button1Colour, button2Colour, button3Colour, button4Colour, button5Colour = DEFAULT_COLOUR, DEFAULT_COLOUR, DEFAULT_COLOUR, DEFAULT_COLOUR, DEFAULT_COLOUR

window = master.Tk()
window.geometry("1000x500")

mainmenu = master.Menu()
mainmenu.add_command(label="Reset", command=reset)

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

button1 = master.Button(command=changeColourButton1, bg=button1Colour)
button2 = master.Button(command=changeColourButton2, bg=button2Colour)
button3 = master.Button(command=changeColourButton3, bg=button3Colour)
button4 = master.Button(command=changeColourButton4, bg=button4Colour)
button5 = master.Button(command=changeColourButton5, bg=button5Colour)

button1.config(width=BUTTON_WIDTH)
button2.config(width=BUTTON_WIDTH)
button3.config(width=BUTTON_WIDTH)
button4.config(width=BUTTON_WIDTH)
button5.config(width=BUTTON_WIDTH)

button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button4.grid(row=2, column=3)
button5.grid(row=2, column=4)

goButton = master.Button(command=start, bg="cyan", text="Go!")
goButton.config(width=2*BUTTON_WIDTH)
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
