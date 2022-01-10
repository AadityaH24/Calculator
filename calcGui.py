# Make gui for calculator
# import calc class

from calc import Calculator

# make gui
from tkinter import Tk, Label, Button, Entry

class CalcGui:
    def __init__(self, master):
        self.master = master
        master.title("A simple Calculator")
        self.Calc = Calculator()

        # calc output label
        self.label = Label(master, text=self.Calc.result)
        self.label.pack()


        #Create an Entry widget to accept User Input
        entry= Entry(master, width= 40)
        entry.focus_set()
        entry.pack()

        #Create buttons for basic calc functions
        self.add_button = Button(master, text="Add", command=lambda: self.add(int(entry.get())))
        self.add_button.pack()

        self.subtract_button = Button(master, text="Subtract", command=lambda: self.subtract(int(entry.get())))
        self.subtract_button.pack()

        self.multiply_button = Button(master, text="Multiply", command=lambda: self.multiply(int(entry.get())))
        self.multiply_button.pack()

        self.divide_button = Button(master, text="Divide", command=lambda: self.divide(int(entry.get())))
        self.divide_button.pack()

        self.clear_button = Button(master, text="Clear", command=lambda: self.clear(int(entry.get())))
        self.clear_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def add(self, num):
        self.Calc.add(num)
        self.label.config(text=self.Calc.result)
    def subtract(self, num):
        self.Calc.subtract(num)
        self.label.config(text=self.Calc.result)
    def multiply(self, num):
        self.Calc.multiply(num)
        self.label.config(text=self.Calc.result)
    def divide(self, num):
        self.Calc.divide(num)
        self.label.config(text=self.Calc.result)
    def clear(self, num):
        self.Calc.result = 0
        self.label.config(text=self.Calc.result)

root = Tk()
my_gui = CalcGui(root)
root.mainloop()