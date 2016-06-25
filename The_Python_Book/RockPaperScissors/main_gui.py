#!/usr/bin/env python3

# Creates the overall interface to access the game

from Tkinter import *

import rps_2_gui

root=Tk()
root.title("Jen's games")

mainframe=Frame(root,height=200,width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5,pady=5)

intro=Label(mainframe,text="""Welcome to Jen's Games. Please make your (RPS) choice.""")
intro.pack(side=TOP)

rps_button=Button(mainframe,text="Rock,Paper,Scissors", command=rps_2_gui.gui)
rps_button.pack()

test_button=Button(mainframe,text="Test Button")
test_button.pack()

exit_button=Button(mainframe,text="Quit", command=root.destroy)
exit_button.pack(side=BOTTOM)

root.mainloop()
