import random
import tkinter as tk
import os

def generate(num):
    global numbersRandomL
    try:
        num = int(num)
        num2 = ''
        for i in range(num):
            num3 = random.randint(0, 9)
            num2 += str(num3)
        numbersRandomL.destroy()
        numbersRandomL = tk.Label(window, text = num2)
        numbersRandomL.pack()
    except ValueError:
        numbersRandomL.destroy()
        numbersRandomL = tk.Label(window, text = 'Incorrect input. Enter an integer')
        numbersRandomL.pack()

window = tk.Tk()
window.geometry('350x200')
window.title('Number Generator')

dirpath = os.getcwd()
photo = tk.PhotoImage(file = dirpath + '/resources/numbers.gif')
gifL = tk.Label(window, image = photo)
gifL.pack()
numbersL = tk.Label(window, text = 'Enter how many numbers you want to generate')
numbersL.pack()
numbersE = tk.Entry(window)
numbersE.pack()
generateB = tk.Button(window, text = 'Generate', command = lambda: generate(numbersE.get()))
generateB.pack()
numbersRandomL = tk.Label(window, text = '')
numbersRandomL.pack()

window.mainloop()
