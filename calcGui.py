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
        self.label.grid(row=0, column=0, columnspan=4)


        #Create an Entry widget to accept User Input
        self.entry = Entry(master, width= 40)
        self.entry.focus_set()
        self.entry.grid(row=1, column=0, columnspan=4)


        # buttons to set number in entry
        self.button_1 = Button(master, text="1", command=lambda: self.set_value(1))
        self.button_1.grid(row=2, column=5)
        self.button_2 = Button(master, text="2", command=lambda: self.set_value(2))
        self.button_2.grid(row=2, column=6)
        self.button_3 = Button(master, text="3", command=lambda: self.set_value(3))
        self.button_3.grid(row=2, column=7)
        self.button_4 = Button(master, text="4", command=lambda: self.set_value(4))
        self.button_4.grid(row=3, column=5)
        self.button_5 = Button(master, text="5", command=lambda: self.set_value(5))
        self.button_5.grid(row=3, column=6)
        self.button_6 = Button(master, text="6", command=lambda: self.set_value(6))
        self.button_6.grid(row=3, column=7)
        self.button_7 = Button(master, text="7", command=lambda: self.set_value(7))
        self.button_7.grid(row=4, column=5)
        self.button_8 = Button(master, text="8", command=lambda: self.set_value(8))
        self.button_8.grid(row=4, column=6)
        self.button_9 = Button(master, text="9", command=lambda: self.set_value(9))
        self.button_9.grid(row=4, column=7)
        self.button_0 = Button(master, text="0", command=lambda: self.set_value(0))
        self.button_0.grid(row=5, column=5, columnspan=3)




        #Create buttons for basic calc functions
        self.add_button = Button(master, text="Add", command=lambda: self.add(int(self.entry.get())))
        self.add_button.grid(row=2, column=0)

        self.subtract_button = Button(master, text="Subtract", command=lambda: self.subtract(int(self.entry.get())))
        self.subtract_button.grid(row=2, column=1)

        self.multiply_button = Button(master, text="Multiply", command=lambda: self.multiply(int(self.entry.get())))
        self.multiply_button.grid(row=2, column=2)

        self.divide_button = Button(master, text="Divide", command=lambda: self.divide(int(self.entry.get())))
        self.divide_button.grid(row=2, column=3)

        self.clear_button = Button(master, text="Clear", command=lambda: self.clear())
        self.clear_button.grid(row=3, column=0)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=3, column=2)


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
    def clear(self):
        self.Calc.result = 0
        self.entry.delete(0, 'end')
        self.label.config(text=self.Calc.result)

    # set value for entry
    def set_value(self, num):
        self.entry.insert(0, num)

root = Tk()
my_gui = CalcGui(root)
root.mainloop()