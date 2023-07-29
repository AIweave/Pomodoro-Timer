from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timerstart = None  # makes timer a global variable for later use; use None instead of 0 since its not an int datatype

# ---------------------------- TIMER RESET ------------------------------- #
##TODO CREATE START & RESET BUTTONS, TIMER FUNCTIONALITY (COUNTDOWN, SESSIONS), WINDOW & LABELS

def resetimer():
    windows.after_cancel(timerstart)
    canvas.itemconfig(timer, text="00:00")
    timerlabel.config(text="Timer")
    checklabel.config(text="")
    global reps
    reps = 0

def starttimer():
    global reps
    reps += 1

    worksec = WORK_MIN * 60
    shortsec = SHORT_BREAK_MIN * 60
    longsec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(longsec)
        timerlabel.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(shortsec)
        timerlabel.config(text="BREAK", fg=PINK)
    else:
        countdown(worksec)
        timerlabel.config(text="WORK", fg=GREEN)


def countdown(count):
    countmin = math.floor(count / 60)
    countsec = count % 60

    if countsec < 10:
        countsec = f"0{countsec}"
    canvas.itemconfig(timer, text=f"{countmin}:{countsec}")
    if count > 0:
        global timerstart
        timerstart = windows.after(1000, countdown, count - 1)
    else:
        starttimer()
        mark = ""
        session = math.floor(reps/2)
        for _ in range(session):
            mark += "✓"
        checklabel.config(text=mark)

windows = Tk()
windows.title("Pomodoro Kit")
windows.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 40, "normal"))
canvas.grid(column=1, row=1)

timerlabel = Label()
timerlabel.config(text="Timer", font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
timerlabel.grid(column=1, row=0)

start = Button()
start.config(text="START", font=(FONT_NAME, 20, "normal"), highlightthickness=0, command=starttimer)
start.grid(column=0, row=4)
reset = Button()
reset.config(text="RESET", font=(FONT_NAME, 20, "normal"), highlightthickness=0, command=resetimer)
reset.grid(column=4, row=4)

checklabel = Label()
checklabel.config(fg=GREEN, bg=YELLOW)
checklabel.grid(column=1, row=4)


windows.mainloop()
