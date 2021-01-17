from tinydb import TinyDB, Query
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext 

class EventManagerApp():
    def __init__(self,master):
        self.master = master 
        self.master.geometry('300x250')

    def labels(self):
        name_label = tk.Label(self.master, text="Name")
        name_label.place(x=0,y=0)

        number_label = tk.Label(self.master, text="Number")
        number_label.place(x=0,y=30)

        tag_label = tk.Label(self.master, text="Tag")
        tag_label.place(x=0,y=60)

        name_entry = tk.Entry(self.master)
        name_entry.place(x=100,y=0)

        number_entry = tk.Entry(self.master)
        number_entry.place(x=100,y=30)        

    def tag_chooser(self):
        choices = ['Platinum Purple', 'Basic Blue']
        chooser = tk.ttk.Combobox(self.master,values = choices)
        chooser.current(1)
        chooser.place(x=100, y=60)

    def display_output(self):
        self.output_window.configure(state=tk.NORMAL)
        self.output_window.insert(tk.INSERT,"Hello\n")
        self.output_window.configure(state=tk.DISABLED)

    def confirmation_button(self):
        check = tk.Button(self.master,text='Show', command=self.display_output)
        check.place(x=25,y = 100,width=250)


    def output(self):
        self.output_window=scrolledtext.ScrolledText(self.master, width=70, height=70, wrap=tk.WORD,state=tk.DISABLED)
        self.output_window.place(x=25,y=130,width=250,height=100)
    
    def process(self):
        pass

    def run(self):
        self.labels()
        self.tag_chooser()
        self.confirmation_button()
        self.output()
        self.master.mainloop()
        pass

if __name__ == "__main__":
    master = tk.Tk()
    master.title("Accentrist Media")
    app = EventManagerApp(master)
    app.run()
