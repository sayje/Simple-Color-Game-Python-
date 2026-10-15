from .handler import *
import ColorGame.state as state

def init():
    window.protocol("WM_DELETE_WINDOW", close_window)

    state.colorRand = state.threading.Thread(target=rolling)

    update_wallet()

    ctl["winning_colors"] = []
    ctl["result_colors"] = []
    ctl["colors"] = []

    #
    # == Start Menu == #
    #

    ctl["start_menu"] = Frame(window, bg="black")
    ctl["start_menu"].pack(expand=True, fill="both")
    # ctl["start_menu"].pack_forget()

    ctl["title_box"] = Frame(ctl["start_menu"], bg=ctl["start_menu"]["bg"])
    ctl["title_box"].pack(fill="x", pady=[96, 0])

    ctl["label_box"] = Frame(ctl["title_box"], bg=ctl["start_menu"]["bg"])
    ctl["label_box"].pack(expand=True)

    ctl["game_title_1"] = Label(ctl["label_box"], text="COLOR", font="Arial 64 bold", bg=ctl["label_box"]["bg"], fg="white")
    ctl["game_title_1"].pack()
    ctl["game_title_2"] = Label(ctl["label_box"], text="GAME", font="Arial 48 bold", bg=ctl["label_box"]["bg"], fg="white")
    ctl["game_title_2"].pack()

    ctl["start_btn"] = Button(ctl["start_menu"], bd=0, text="START GAME", font="Arial 24 bold", command=start_game)
    ctl["start_btn"].pack(expand=True, ipadx=24, ipady=8)

    #
    # == Main Window == #
    #

    ctl["main_window"] = Frame(window, bg="black")
    ctl["main_window"].pack_forget()
    # ctl["main_window"].pack(expand=True, fill="both")

    # Pocket Money

    ctl["pm_root"] = Frame(ctl["main_window"], bg=ctl["main_window"]["bg"])
    ctl["pm_root"].pack(fill="x", ipady=24)

    ctl["pm_box"] = Frame(ctl["pm_root"], bg=ctl["main_window"]["bg"])
    ctl["pm_box"].pack(expand=True)

    Label(
        ctl["pm_box"], text="Pocket Money", font=fs, fg="gold", bg=ctl["main_window"]["bg"]
    ).pack()
    
    Label(
        ctl["pm_box"], textvariable=walletAmount, font="Arial 40 bold", fg="white", bg=ctl["main_window"]["bg"]
    ).pack()

    # Dice

    ctl["rand_box"] = Frame(ctl["main_window"], bg=ctl["main_window"]["bg"])
    ctl["rand_box"].pack(fill="x", ipady=16)
    # ctl["rand_box"].pack_forget()

    ctl["dice"] = Label(ctl["rand_box"], width=8, height=4, bg="gray")
    ctl["dice"].pack(expand=True)

    # Winning Colors

    ctl["winning_root"] = Frame(ctl["main_window"], bg=ctl["main_window"]["bg"])
    ctl["winning_root"].pack(fill="x", ipady=8)
    # ctl["winning_root"].pack_forget()

    ctl["winning_box"] = Frame(ctl["winning_root"], bg=ctl["winning_root"]["bg"])
    ctl["winning_box"].pack(expand=True)
    
    Label(
        ctl["winning_box"], text="Winning Colors", font=fs, bg=ctl["winning_root"]["bg"], fg="gold"
    ).grid(row=0, column=0, columnspan=3)

    for i in range(3):
        _color = Label(ctl["winning_box"], width=4, height=2, bg="gray")
        _color.grid(row=1, column=i, padx=4, pady=4)
        ctl["winning_colors"].append(_color)

    ctl["roll_btn"] = Button(ctl["winning_box"], bd=0, font="Arial 16 bold", text="ROLL!", command=roll_dice)
    ctl["roll_btn"].grid(row=2, column=0, columnspan=3, ipadx=16, ipady=4, pady=16)
    ctl["roll_btn"]["state"] = "disabled"

    # Colors

    ctl["color_root"] = Frame(ctl["main_window"], bg="#090909")
    ctl["color_root"].pack(expand=True, fill="both")
    # ctl["color_root"].pack_forget()

    ctl["color_box"] = Frame(ctl["color_root"], bg=ctl["color_root"]["bg"])
    ctl["color_box"].pack(expand=True)
    # ctl["color_box"].pack_forget()

    for i in range(len(listColors)):
        bets[i].set(0)
        _color = Button(ctl["color_box"], textvariable=bets[i], bd=0, font="Arial 24 bold", bg=listColors[i], width=5, height=2, command=lambda arg=i: choose_color(arg))
        _row = int(i / 3)
        _color.grid(row=_row, column=(i - (_row * 3)), pady=2, padx=2)
        ctl["colors"].append(_color)

    ctl["bet_box"] = Frame(ctl["color_root"], bg=ctl["color_root"]["bg"])
    # ctl["bet_box"].pack(expand=True, fill="both")
    ctl["bet_box"].pack_forget()

    ctl["bet_left"] = Frame(ctl["bet_box"], bg=ctl["color_root"]["bg"], width=240)
    ctl["bet_left"].pack(side=LEFT, anchor="w", expand=True, fill="y")
    ctl["bet_left"].pack_propagate(0)

    ctl["bet_right"] = Frame(ctl["bet_box"], bg="#121212", width=240)
    ctl["bet_right"].pack(side=RIGHT, anchor="e", expand=True, fill="y")
    ctl["bet_right"].pack_propagate(0)

    # [Betting] Left Side

    ctl["selected"] = Label(ctl["bet_left"], bg="gray", width=18, height=9)
    ctl["selected"].pack(expand=True)

    # [Betting] Right Side

    ctl["bet_right_box"] = Frame(ctl["bet_right"], bg=ctl["bet_right"]["bg"])
    ctl["bet_right_box"].pack(expand=True)

    Label(
        ctl["bet_right_box"], text="Bet Amount", font=fs, fg="gold", bg=ctl["bet_right_box"]["bg"]
    ).pack(ipady=8)
    
    vcmd = (window.register(num_input))
    ctl["bet_amount"] = Entry(ctl["bet_right_box"], bd=0, justify=CENTER, textvariable=betAmount, font="Arial 32 bold", validate="all", validatecommand=(vcmd, "%P"))
    ctl["bet_amount"].pack(padx=32)

    ctl["bet_btn"] = Button(ctl["bet_right_box"], text="SAVE", font="Arial 16 bold", bd=0, command=place_bets)
    ctl["bet_btn"].pack(pady=[32, 0], ipadx=16, ipady=4)

    # Result

    ctl["result_root"] = Frame(ctl["main_window"], bg="#090909")
    ctl["result_root"].pack_forget()
    # ctl["result_root"].pack(expand=True, fill="both")

    ctl["result_box"] = Frame(ctl["result_root"], bg=ctl["result_root"]["bg"])
    ctl["result_box"].pack(expand=True)

    Label(
        ctl["result_box"], text="Results", font="Arial 36 bold", fg="gold", bg=ctl["result_box"]["bg"]
    ).grid(row=0, column=0, columnspan=3, pady=[0, 48])

    for i in range(3):
        results[i].set(0)
        _color = Label(ctl["result_box"], width=12, height=6, bg="gray")
        _color.grid(row=1, column=i, padx=8, pady=8)
        ctl["result_colors"].append(_color)
        
        Label(
            ctl["result_box"], textvariable=results[i], bg=ctl["result_box"]["bg"], fg="white", font="Arial 24 bold"
        ).grid(row=2, column=i, padx=8, pady=[0, 32])

    Label(
        ctl["result_box"], bg=ctl["result_box"]["bg"], textvariable=resultMsg, font="Arial 24", fg="cyan"
    ).grid(row=3, column=0, columnspan=3, pady=[0, 24])

    ctl["close_btn"] = Button(ctl["result_box"], text="CLOSE", font="Arial 16 bold", bd=0, command=close_results)
    ctl["close_btn"].grid(row=4, column=0, columnspan=3, ipadx=16, ipady=2)

    state.threading.Thread(target=animate_title, daemon=True).start()

    #
    # Game Over
    #

    ctl["game_over"] = Frame(window, bg="black")
    ctl["game_over"].pack_forget()
    # ctl["game_over"].pack(expand=True, fill="both")

    Label(ctl["game_over"], text="GAME OVER", font="Arial 36 bold", bg=ctl["game_over"]["bg"], fg="gold").pack(expand=True)
    ctl["exit_btn"] = Button(ctl["game_over"], text="EXIT GAME", bd=0, font="Arial 24 bold", command=lambda: exit())
    ctl["exit_btn"].pack(expand=True, ipadx=16, ipady=2)