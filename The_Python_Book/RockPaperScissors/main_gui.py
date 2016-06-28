#!/usr/bin/env python3

# Creates the overall interface to access the game
from tkinter import *
from tkinter.ttk import *
import random
import rps_gui_python3_withmain

main=Tk()
main.title("Jen's games")

mainframe=Frame(main,height=200,width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5,pady=5)

intro=Label(mainframe,text="""Welcome to Jen's Games. Please make your (RPS) choice.""")
intro.pack(side=TOP)

rps_button=Button(mainframe,text="Rock,Paper,Scissors", command=rps_gui_python3_withmain.gui)
rps_button.pack()

test_button=Button(mainframe,text="Test Button")
test_button.pack()

exit_button=Button(mainframe,text="Quit", command=main.destroy)
exit_button.pack(side=BOTTOM)

main.mainloop()
