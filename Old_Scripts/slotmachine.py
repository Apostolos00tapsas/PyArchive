import tkinter as tk
import random

intro = """Panther's Den Slot Machine.


Welcome to my den!

You can win by rolling Ocelots, Jaguars, Boas, Caimans, Macaws or Tapirs.
You can also with big with three Ibis.

You'll lose a coin for anything else, and if you roll three Scorpions say good bye to 500 coins

Good luck kit!"""



root = tk.Tk()
root.geometry("700x400")
root.title("Slot Machine")
root.configure(background='seagreen')

INIT_STAKE = 100
ITEMS = ["OCELOT", "MACAW", "JAGUAR", "IBIS", "CAIMAN", "BOA", "SCORPION", "TAPIR", "CONDOR", "BAMBOO", "FROG"]

first = None
second = None
third = None
stake = INIT_STAKE

nameLabel = tk.Label(root, text="PANTHER DEN", font=('Cambria', 60))
nameLabel.pack()
lbl = tk.Label(root, text=intro, background='seagreen', font=('Cambria', 12))
lbl.pack()
lbl2 = tk.Label(root, text=stake)
lbl2.pack()

def play():
    global first, second, third
    first = spin()
    second = spin()
    third = spin()
    score()

def quit_play():
    lbl.config(text="Game has ended. You won a total of " + str(stake) + " coins")

def spin():
    randomnumber = random.randint(0, 10)
    return ITEMS[randomnumber]

def score():
    global stake, first, second, third
    if((first == "OCELOT") and (second != "MACAW")):
        win = 5
    elif((first == "JAGUAR") and (second == "JAGUAR") and (third != "JAGUAR")):
        win = 8
    elif((first == "BOA") and (second == "BOA") and (third == "BOA")):
        win = 10
    elif((first == "CAIMAN") and (second == "CAIMAN") and ((third == "CAIMAN") or (third == "BOA"))):
        win = 8
    elif((first == "MACAW") and (second == "IBIS") and ((third == "MACAW"))):
        win = 15
    elif((first == "TAPIR") and (second == "TAPIR") and ((third == "TAPIR"))):
        win = 20
    elif((first == "IBIS") and (second == "IBIS") and (third == "IBIS")):
        win = 300
    elif((first == "SCORPION") and (second == "SCORPION") and (third == "SCORPION")):
        win = -500
    else:
        win = -1

    stake += win

    if(win > 0):
        lbl.config(text="{}\t{}\t{} -- You win {} Coins".format(first, second, third, win))
        lbl2.config(text=stake)
    else:
        lbl.config(text="{}\t{}\t{} -- You lose".format(first, second, third))
        lbl2.config(text=stake)

tk.Button(root, text="Play", command=play).pack()

root.mainloop()
