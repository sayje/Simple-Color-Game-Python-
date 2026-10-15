import threading

pocketMoney = 500
winningColors = []
selectedColor = -1

ev = threading.Event()
colorRand = None