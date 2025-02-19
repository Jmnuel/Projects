import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def evaluate_postfix(expression):
    stack = Stack()
    for token in expression:
        if token.isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(add(a, b))
            elif token == '-':
                stack.push(subtract(a, b))
            elif token == '*':
                stack.push(multiply(a, b))
            elif token == '/':
                stack.push(divide(a, b))
    return stack.pop()

def shunting_yard(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    output = []
    for token in expression:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (not stack.is_empty() and stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
    while not stack.is_empty():
        output.append(stack.pop())
    return output

def calculate():
    try:
        expression = entry.get()
        if not expression:
            messagebox.showwarning("Input Error", "Please enter an expression.")
            return

        tokens = expression.split()
        postfix = shunting_yard(tokens)
        result = evaluate_postfix(postfix)
        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Math Error", str(e))
    except IndexError:
        messagebox.showerror("Syntax Error", "Invalid expression. Please check your input.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

root = tk.Tk()
root.title("Simple Calculator")

root.geometry("400x450")  

logo_image = Image.open("logo.png")  
logo_image = logo_image.resize((150, 100), Image.Resampling.LANCZOS)  
logo_photo = ImageTk.PhotoImage(logo_image) 

logo_label = tk.Label(root, image=logo_photo)
logo_label.image = logo_photo 
logo_label.pack(pady=10) 

example_label = tk.Label(root, text="Example: 3 + 5 * ( 2 - 8 )", font=("Arial", 10), fg="gray")
example_label.pack(pady=5) 

entry = tk.Entry(root, width=50)
entry.pack(pady=10) 

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10) 

result_label = tk.Label(root, text="Result: ", font=("Arial", 12,))
result_label.pack(pady=20)  

root.mainloop()