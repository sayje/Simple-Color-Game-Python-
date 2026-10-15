from .constants import *
from .handler import place_bets

def _apply(btn, ev, bg, fg):
    btn.bind(ev, lambda event: btn["state"] == "normal" and btn.configure(bg=bg, fg=fg))

def apply():
    ctl["bet_amount"].bind("<Return>", lambda args=[]: place_bets())

    for l in ["start_btn", "roll_btn"]:
        ctl[l].configure(bg="#c62f0f", fg="white")

        if l == "start_btn":
            ctl[l].configure(activebackground="#cf0000", activeforeground="gold")
            _apply(ctl[l], "<Enter>", bg="#cf1313", fg="yellow")
        else:
            ctl[l].configure(activebackground="yellow", activeforeground="black")
            _apply(ctl[l], "<Enter>", bg="gold", fg="black")

        _apply(ctl[l], "<Leave>", bg="#c62f0f", fg="white")

    ctl["bet_btn"].configure(bg="#2d2d2d", fg="#1dd92b", activebackground="#019f0d", activeforeground="#b0ffb6")
    _apply(ctl["bet_btn"], "<Enter>", bg="#00a60c", fg="white")
    _apply(ctl["bet_btn"], "<Leave>", bg="#2d2d2d", fg="#1dd92b")

    for l in ["close_btn", "exit_btn"]:
        ctl[l].configure(bg="#181818", fg="#ff3434", activebackground="#c21515", activeforeground="yellow")
        _apply(ctl[l], "<Enter>", bg="#cf1313", fg="white")
        _apply(ctl[l], "<Leave>", bg="#181818", fg="#ff3434")