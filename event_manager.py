import re
from tinydb import TinyDB, Query
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext 

class EventManagerApp():
    def __init__(self,master):
        self.master = master 
        self.master.geometry('300x250')
        self.paid = {}
        self.db = TinyDB('db.json')

    def labels(self):
        """
        Set up all necessary labels
        """

        name_label = tk.Label(self.master, text="Name")
        name_label.place(x=0,y=0)

        number_label = tk.Label(self.master, text="Number")
        number_label.place(x=0,y=30)

        tag_label = tk.Label(self.master, text="Tag")
        tag_label.place(x=0,y=60)
    

    def entry_field(self):
        """
        Set up all necessary entry fields
        """

        self.name_entry = tk.Entry(self.master)
        self.name_entry.place(x=100,y=0)

        self.number_entry = tk.Entry(self.master)
        self.number_entry.place(x=100,y=30)        

    def get_name(self):
        """
        Gets entry name
        """

        return self.name_entry.get()
    
    def get_number(self):
        """
        Gets entry number
        """
        return self.number_entry.get()

    def tag_chooser(self):
        """
        Sets up the tag spinner with the available tickets
        """

        choices = ['Platinum Purple', 'Basic Blue']
        chooser = tk.ttk.Combobox(self.master,values = choices)
        chooser.current(1)
        chooser.place(x=100, y=60)


    def confirmation_message(self):
        response = messagebox.askquestion("askquestion", "Are you sure?")
        self.tag = "purple"
        if response == "yes":
            self.write_to_db()
            self.display_paid_output()


    def write_to_db(self):
        self.db.insert({'name':self.name,'number':self.number})

    def display_check_output(self):
        """
        Display requested information and price and RSVP
        """

        entry_name = self.get_name()
        entry_number = self.get_number()
        self.name = ""
        self.number = ""

        if re.match("^((?:\+27|27)|0)(\d{2})-?(\d{3})-?(\d{4})$",entry_number) and entry_name != "":
            self.name = entry_name.strip()
            self.number = entry_number
        elif entry_name == "":
            text = "Incorrect name"
            messagebox.showerror(title="Invalid Entry", message=text)
        else:
            text = "Incorrect number"
            messagebox.showerror(title="Invalid Entry", message=text)

        self.check_window.configure(state=tk.NORMAL)
        self.paid[self.name]=self.number
        self.info = f'{self.name} {self.number}'
        self.check_window.insert(tk.INSERT,self.info)
        self.check_window.configure(state=tk.DISABLED)


    def display_paid_output(self): 
        """
        Output payment info and customer details
        """

        self.paid_window.configure(state=tk.NORMAL)
        if self.info !="":
           self.paid_window.insert(tk.INSERT,self.info+"\n")

        self.check_window.configure(state=tk.NORMAL)
        self.check_window.delete('1.0', tk.END)

        self.name_entry.delete(0,tk.END)
        self.number_entry.delete(0,tk.END)        
        self.info = ""
        self.check_window.configure(state=tk.DISABLED)

        self.paid_window.configure(state=tk.DISABLED)


    def check_button(self):
        """
        Button to check RSVP and price
        """

        check = tk.Button(self.master,bg='red',text='Check', command=self.display_check_output)
        check.place(x=25,y = 100,width=125,height=30)


    def paid_button(self):
        """
        Button to confirm payment for diplayed price
        """

        paid = tk.Button(self.master,bg='green',text='Paid', command=self.confirmation_message)#self.display_paid_output)
        paid.place(x=150,y = 100,width=125)


    def check_output(self):
        """
        Setup for the checking output
        """

        self.check_window = tk.Text(self.master,state=tk.DISABLED)
        self.check_window.place(x=25,y=130,width=250,height=100)

    def paid_output(self):
        """
        Setup for displaying paid output
        """

        self.paid_window=scrolledtext.ScrolledText(self.master,bg="lawn green", width=70, height=70, wrap=tk.WORD,state=tk.DISABLED)
        self.paid_window.place(x=25,y=160,width=250,height=100)


    def get_info(self):
        """
        self.name = self.name_entry.get()
        self.display_check_output()
        """
        pass

    def run(self):
        self.labels()
        self.entry_field()
        self.tag_chooser()
        self.check_button()
        self.paid_button()
        self.check_output()
        self.paid_output()
        self.display_check_output()
        self.display_paid_output()
        self.master.mainloop()
        pass

if __name__ == "__main__":
    master = tk.Tk()
    master.title("Accentrist Media")
    app = EventManagerApp(master)
    app.run()
