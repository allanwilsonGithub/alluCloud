#! /usr/bin/env python
#GUI

import sys
import console_actions_events
import console_actions_films
import console_actions_notes
import console_actions_total_backup
import Tkinter
from Tkinter import *

class App:

    def __init__(self, master):
        frame = Frame(master)

        Label(frame, text="Events", width=50).pack(side=TOP)

        self.action1 = Button(frame, text="Add Event", fg="SeaGreen", command=self.action1)
        self.action1.pack(side=TOP)

        Label(frame, text="Films").pack(side=TOP)
        self.action2 = Button(frame, text="Add Unseen Film", fg="SeaGreen", command=self.action2)
        self.action2.pack(side=TOP)

        self.action3 = Button(frame, text="Update Film to Seen", fg="SlateGrey", command=self.action3)
        self.action3.pack(side=TOP)

        Label(frame, text="Books").pack(side=TOP)
        self.action4 = Button(frame, text="Add Book", fg="SlateGrey", command=self.action4)
        self.action4.pack(side=TOP)
        
        Label(frame, text="Web").pack(side=TOP)
        self.action5 = Button(frame, text="Add Web Search Term", fg="SlateGrey", command=self.action5)
        self.action5.pack(side=TOP)
        self.action6 = Button(frame, text="Add URL to check", fg="SlateGrey", command=self.action6)
        self.action6.pack(side=TOP)
        
        Label(frame, text="Notes").pack(side=TOP)
        self.action7 = Button(frame, text="Add note", fg="SeaGreen", command=self.action7)
        self.action7.pack(side=TOP)
        self.action8 = Button(frame, text="Delete note", fg="SeaGreen", command=self.action8)
        self.action8.pack(side=TOP)
        self.action9 = Button(frame, text="List notes", fg="SeaGreen", command=self.action9)
        self.action9.pack(side=TOP)

        Label(frame, text="TotalBackup").pack(side=TOP)
        self.action10 = Button(frame, text="Delete USB HDD and copy everything again", fg="SeaGreen", command=self.action10)
        self.action10.pack(side=TOP)
        self.action11 = Button(frame, text="Delete QNAP HDD and copy everything again", fg="SeaGreen", command=self.action11)
        self.action11.pack(side=TOP)

        self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
        self.button.pack(side=TOP)

        frame.pack()
        
    def action1(self):
        console_actions_events.add_event()

    def action2(self):
        console_actions_films.add_film()

    def action3(self):
        print "Action3 was pressed"

    def action4(self):
        print "Action4 was pressed"

    def action5(self):
        print "Action5 was pressed"

    def action6(self):
        print "Action6 was pressed"

    def action7(self):
        console_actions_notes.add_note()

    def action8(self):
        console_actions_notes.delete_note()

    def action9(self):
        console_actions_notes.list_notes()

    def action10(self):
        console_actions_total_backup.delete_backup_and_recopy_to_USB_HDD()

    def action11(self):
        console_actions_total_backup.delete_backup_and_recopy_to_QNAP_HDD()


root = Tk()
root.title("AlluCloud")

app = App(root)
 
root.mainloop()
