from tkinter import *

listColors = ("RED", "GREEN", "BLUE", "PINK", "YELLOW", "WHITE")
fs = "Arial 12"
ctl = {}

window = Tk()
walletAmount = StringVar()
betAmount = IntVar()
bets = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
results = [IntVar(), IntVar(), IntVar()]
resultMsg = StringVar()