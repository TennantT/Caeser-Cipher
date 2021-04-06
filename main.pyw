alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y","z"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
poss = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
posso = ""
string = ""
#string = str(input("Text to be deciphered: "))
def caeser(string, alpha, alphab, a):
    nstring = ""
    alen = len(string)
    for x in range(alen):
        blen = len(alpha)
        for y in range(blen):
            if string[x] == alpha[y] or string[x] == alphab[y]:
                b = y + a
        while b > 26:
            b = b - 26
        nstring = (nstring + alpha[b-1])
    poss[a-1] = nstring
from tkinter import *
import tkinter
def op2():
    main2 = Tk()
    main2.title("Caeser Decryptor")
    main2.configure(background = "#e3f2a0")
    posso = ""
    for c in range(26):
        posso = f"{posso}{poss[c]}\n"
    Message(main2, text = f"{posso}", bg = "#e3f2a0", fg = "#000000", font = "none 12 bold") .grid(row = 1, column = 1, sticky = E)
    Button(main2, text = "REPEAT", width = 10, command = op1()) .grid(row = 2, column = 1, sticky = E)
def op1():
    main = Tk()
    main.title("Caeser Decryptor")
    main.configure(background = "#e3f2a0")
    Label(main, text = "Encrypted Text:", bg = "#e3f2a0", fg = "#000000", font = "none 12 bold") .grid(row = 1, column = 0, sticky = E)
    string_entry = Entry(main, width = 40, bg = "#ffffff")
    string_entry.grid(row = 1, column = 1, sticky = E)
    def click():
        string = string_entry.get()
        for a in range(26):
            caeser(string, alpha, alphab, a)
        main.destroy()
        op2()
    Button(main, text = "DECRYPT", width = 10, command = click) .grid(row = 3, column = 1, sticky = E)
    main.mainloop()
op1()
