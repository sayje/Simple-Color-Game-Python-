import time
import random
import ColorGame.state as state
from .constants import *

_animate_ev = state.threading.Event()

def update_wallet():
    walletAmount.set("P %d" % (state.pocketMoney))

def num_input(v):
    return str.isdigit(v) or v == ""

#########

def animate_title():
    while not _animate_ev.is_set():
        time.sleep(0.2)
        ctl["game_title_1"].configure(fg=random.choice(listColors))
        ctl["game_title_2"].configure(fg=random.choice(listColors))

def close_window():
    _animate_ev.set()
    window.destroy()

def start_game():
    _animate_ev.set()
    ctl["start_menu"].pack_forget()
    ctl["main_window"].pack(expand=True, fill="both")

#########

def validate_roll():
    for _b in bets:
        if _b.get() > 0:
            ctl["roll_btn"]["state"] = "normal"
            return
    
    ctl["roll_btn"]["state"] = "disabled"

def choose_color(idx):
    ctl["roll_btn"]["state"] = "disabled"
    ctl["color_box"].pack_forget()
    ctl["bet_box"].pack(expand=True, fill="both")
    state.selectedColor = idx

    ctl["selected"].configure(bg=listColors[idx])
    betAmount.set(bets[idx].get())

    ctl["bet_amount"].focus()
    ctl["bet_amount"].icursor("end")

    if betAmount.get() < 1:
        ctl["bet_amount"].select_range(0, "end")

def place_bets():
    _diff = 0
    try:
        _diff = betAmount.get() - bets[state.selectedColor].get()
        if _diff > state.pocketMoney:
            betAmount.set(bets[state.selectedColor].get())
            _diff = 0
    except:
        betAmount.set(0)

    state.pocketMoney -= _diff
    update_wallet()

    bets[state.selectedColor].set(betAmount.get())
    state.selectedColor = -1
    betAmount.set(0)
    ctl["selected"].configure(bg="gray")

    ctl["bet_box"].pack_forget()
    ctl["color_box"].pack(expand=True)

    validate_roll()

def close_results():
    if state.pocketMoney < 1:
        ctl["main_window"].pack_forget()
        ctl["game_over"].pack(expand=True, fill="both")
        return

    update_wallet()
    
    ctl["result_root"].pack_forget()
    ctl["rand_box"].pack(fill="x", ipady=16)
    ctl["winning_root"].pack(fill="x", ipady=8)
    ctl["color_root"].pack(expand=True, fill="both")

    for i in range(3):
        ctl["result_colors"][i].configure(bg="gray")
        results[i].set(0)

    resultMsg.set("")

def _roll_finish():
    for k in ["rand_box", "winning_root", "color_root"]:
        ctl[k].pack_forget()

    ctl["result_root"].pack(expand=True, fill="both")

    _totalwins = 0
    _resultIdx = 0

    for i in range(6):
        _count = state.winningColors.count(listColors[i])
        if _count > 0:
            _win = bets[i].get() * _count + bets[i].get()

            ctl["result_colors"][_resultIdx].configure(bg=listColors[i])
            results[_resultIdx].set(_win)
            _resultIdx += 1

            _totalwins += _win

        ctl["colors"][i]["state"] = "normal"
        bets[i].set(0)

    if _totalwins > 0:
        resultMsg.set("You won a total of P %d!" % _totalwins)
    else:
        resultMsg.set("You lost. Better luck next time!")

    state.pocketMoney += _totalwins

def rolling():
    _timeLapse = 0.0
    _color = random.choice(listColors)
    while 1:
        time.sleep(0.1)
        _timeLapse += 0.1
        _color = random.choice(listColors)
        try:
            ctl["dice"].configure(bg=_color)
        except:
            state.ev.set()
            break
        
        if _timeLapse >= 2.0:
            state.winningColors.append(_color)

            _len = len(state.winningColors)
            ctl["winning_colors"][_len - 1].configure(bg=state.winningColors[-1])

            if _len == 3:
                state.ev.set()
                break

            time.sleep(1)
            _timeLapse = 0.0

    _roll_finish()
    
def roll_dice():
    ctl["roll_btn"].configure(bg="#c62f0f", fg="white")

    if state.ev.is_set():
        state.colorRand.join()
        state.ev.clear()
        state.colorRand = None
        state.colorRand = state.threading.Thread(target=rolling)

    ctl["roll_btn"]["state"] = "disabled"

    for _c in ctl["colors"]:
        _c["state"] = "disabled"

    state.winningColors.clear()

    for _c in ctl["winning_colors"]:
        _c.configure(bg="gray")
    state.colorRand.start()
