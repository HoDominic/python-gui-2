# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
import logging
from random import choices
import socket
from tkinter import *

from tkinter import messagebox
from tkinter.ttk import Combobox

from tkinter import ttk
import pandas as pd
import threading
import time
import tkinter as tk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # Functies oproepen!
        self.init_window()
        self.makeConnnectionWithServer()

    # Creation of init_window
    def init_window(self):
        self.master.title("Client GUI")
        self.master.geometry("500x500")
        self.master.resizable(False, False)




     #functies in init_window
        
          #Log out as client
        def log_out_client():
            messagebox.askyesno("Log out", "Log out as client?")



        #Tabs
         #TABS
        my_tabs = ttk.Notebook(self.master)
        my_tabs.pack(pady=15)

        tab1 = Frame(my_tabs,width=500,height=500)
        tab1.pack(fill='both', expand=1)
        tab2 = Frame(my_tabs,width=500,height=500 )
        tab2.pack(fill='both', expand=1)

        tab3 = Frame(my_tabs,width=500,height=500 )
        tab3.pack(fill='both', expand=1)

        my_tabs.add(tab1, text='Tab1')
        my_tabs.add(tab2, text='Tab2')
        my_tabs.add(tab3, text='Tab3')


        # Label frames
        wrapper1 = LabelFrame(tab1, text="Clients List")
        wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)

        wrapper2 = LabelFrame(tab1, text="Get data by brand")
        wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

        wrapper3 = LabelFrame(tab1, text="Get amount of brands by calories per serving")
        wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

        wrapper4 = LabelFrame(tab1, text="Get amount of brands by rating")
        wrapper4.pack(fill="both", expand="yes", padx=20, pady=10)

        wrapper5 = LabelFrame(tab1, text="Get amount of brands by sodium")
        wrapper5.pack(fill="both", expand="yes", padx=20, pady=10)

        wrapper6 = LabelFrame(tab2, text="Read admin message")
        wrapper6.pack(fill="both", expand="yes", padx=20, pady=10)

        #log out client button
        btn = Button(wrapper1, text="Log out", command=log_out_client)
        btn.pack(side=tk.LEFT,padx=10 ,pady=0)

        # #get calories by chart button
        # btn = Button(wrapper2, text="Calories by brand", command=get_calories_data_thread)
        # btn.pack(side=tk.LEFT,padx=10 ,pady=0)

        # btn = Button(wrapper2, text="Rating by brand", command=get_rating_data_thread)
        # btn.pack(side=tk.LEFT,padx=20 ,pady=0)

        # btn = Button(wrapper2, text="Sodium by brand", command=get_sodium_data_thread)
        # btn.pack(side=tk.LEFT,padx=30 ,pady=0)


    #WRAPPER3
    # input_calories = Label(wrapper3, text='input minvalue calories')
    # input_calories.pack(side=tk.LEFT, padx=10)
    # entry_client = Entry(wrapper3)
    # entry_client.pack(side=tk.LEFT, padx=10)

    # btn = Button(wrapper3, text="Get data", command=get_calories_with_params_thread)
    # btn.pack(side=tk.LEFT,padx=20 ,pady=0)


    # #WRAPPER4
    # input_rating = Label(wrapper4, text='input minvalue rating')
    # input_rating.pack(side=tk.LEFT, padx=10)
    # entry_client2 = Entry(wrapper4)
    # entry_client2.pack(side=tk.LEFT, padx=10)

    # btn = Button(wrapper4, text="Get data", command=get_ratings_with_params_thread)
    # btn.pack(side=tk.LEFT,padx=20 ,pady=0)

    # #WRAPPER5
    # input_rating = Label(wrapper5, text='input minvalue sodium')
    # input_rating.pack(side=tk.LEFT, padx=10)
    # entry_client3 = Entry(wrapper5)
    # entry_client3.pack(side=tk.LEFT, padx=10)

    # btn = Button(wrapper5, text="Get data", command=get_sodium_with_params_thread)
    # btn.pack(side=tk.LEFT,padx=20 ,pady=0)


    # #WRAPPER6
    # btn = Button(wrapper6, text="Read admin message", command=read_admin_message_thread)
    # btn.pack(side=tk.LEFT,padx=20 ,pady=0)






    # win.destroy()
    # new_window.mainloop()
        #self.pack(fill=BOTH, expand=1)
     

        # Label(self, text="Snelheid (km/u):").grid(row=0)
        # Label(self, text="Reactietijd (sec):", pady=10).grid(row=1)
        # Label(self, text="Type wegdek:", pady=10).grid(row=2)

        # self.entry_snelheid = Entry(self, width=40)
        # self.entry_reactietijd = Entry(self, width=40)
        # self.entry_wegdek = Entry(self, width=40)
        # self.entry_snelheid.grid(row=0, column=1, sticky=E + W, pady=(5, 5))
        # self.entry_reactietijd.grid(row=1, column=1, sticky=E + W)

        # self.label_resultaat = Label(self, width=40, anchor='w')

        # choices = ('Droog wegdek', 'Nat wegdek')
        # # self.entry_wegdek.grid(row=2, column=1, sticky=E + W)
        # self.cbo_wegdek = Combobox(self, state="readonly", width=40)
        # self.cbo_wegdek['values'] = choices
        # self.cbo_wegdek.grid(row=2, column=1, sticky=E + W)

        # #Label(self, text="km/u").grid(row=0, column=2)
        # Label(self, text="m/s").grid(row=0, column=2)
        # Label(self, text="sec", pady=10).grid(row=1, column=2)

        # self.buttonCalculate = Button(
        #     self, text="Bereken stopafstand", command=self.calculateStopafstand)
        # self.buttonCalculate.grid(row=3, column=0, columnspan=3, pady=(
        #     0, 5), padx=(5, 5), sticky=N + S + E + W)

        # Grid.rowconfigure(self, 2, weight=1)
        # Grid.columnconfigure(self, 1, weight=1)

        # root.protocol("WM_DELETE_WINDOW", _delete_window)

    def __del__(self):
        self.close_connection()

    def makeConnnectionWithServer(self):
        try:
            logging.info("Making connection with server...")
            # get local machine name
            host = socket.gethostname()
            port = 9999
            self.socket_to_server = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            # connection to hostname on the port.
            self.socket_to_server.connect((host, port))
            self.my_writer_obj = self.socket_to_server.makefile(mode='rw')
            logging.info("Open connection with server succesfully")
        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")

    def calculateStopafstand(self):
        try:
            snelheid = int(self.entry_snelheid.get())/3.6
            reactietijd = int(self.entry_reactietijd.get())

            wegdek = (self.cbo_wegdek.get())

            if wegdek == "Droog wegdek":
                wegdek = 5
            else:
                wegdek = 8

            print(type(wegdek))

            self.my_writer_obj.write(f"{snelheid}\n")
            logging.info(f"Sending snelheid: {snelheid}")

            self.my_writer_obj.write("%s\n" % reactietijd)
            logging.info(f"Sending reactietijd: {reactietijd}")

            self.my_writer_obj.write("%s\n" % wegdek)
            logging.info(f"Sending wegdek: {wegdek}")

            self.my_writer_obj.flush()

            # waiting for answer
            answer = self.my_writer_obj.readline().rstrip('\n')
            logging.info(f"Answer server: {answer}")
            stopafstand = int(answer)

            self.label_resultaat['text'] = f"{stopafstand}"

        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")
            messagebox.showinfo("Stopafstand berekenen",
                                "Something has gone wrong...")

    def close_connection(self):
        try:
            logging.info("Close connection with server...")
            self.my_writer_obj.write("CLOSE\n")
            self.my_writer_obj.flush()
            self.socket_to_server.close()
        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")
            messagebox.showinfo("Stopafstand berekenen",
                                "Something has gone wrong...")


logging.basicConfig(level=logging.INFO)

root = Tk()
# root.geometry("400x300")
app = Window(root)
root.mainloop()
