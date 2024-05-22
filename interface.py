import tkinter as tk
from math_functions import add, subtract

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.entry1 = tk.Entry(root)
        self.entry2 = tk.Entry(root)
        
        self.entry1.grid(row=0, column=0, padx=10, pady=10)
        self.entry2.grid(row=0, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(root, text="Add", command=self.add)
        self.subtract_button = tk.Button(root, text="Subtract", command=self.subtract)
        
        self.add_button.grid(row=1, column=0, padx=10, pady=10)
        self.subtract_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
    def add(self):
        num1 = self.entry1.get()
        num2 = self.entry2.get()
        result = add(num1, num2)
        self.result_label.config(text="Result: " + str(result))
    
    def subtract(self):
        num1 = self.entry1.get()
        num2 = self.entry2.get()
        result = subtract(num1, num2)
        self.result_label.config(text="Result: " + str(result))
