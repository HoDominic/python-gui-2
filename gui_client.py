# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
import logging
from random import choices
import socket
from struct import pack
from tkinter import *

from tkinter import messagebox
from tkinter.ttk import Combobox

from tkinter import ttk
import pandas as pd
import threading
import time
import tkinter as tk
import mysql.connector


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # Functies oproepen!
        self.init_window()
        self.makeConnnectionWithServer()
        self.makeConnectionWithMysqlDatabase()

    # Creation of init_window
    def init_window(self):
        

#         def add_client():
#             pass



      


        self.pack(fill=BOTH, expand=1)

        var1 = StringVar()
        client_name = StringVar()

        var2 = StringVar()
        client_nickname = StringVar()

        var3 = StringVar()
        client_email = StringVar()
     

        Label(self, text="Client Name:", padx=10, pady=10).grid(row=0)
        #Label(self).grid(column=1)
       
        Label(self, text="Client Nickname:", pady=10).grid(row=1)
        Label(self, text="Client Email:", pady=10).grid(row=2)
      

        self.entry_client_name = Entry(self, width=40)
        self.entry_client_nickname = Entry(self, width=40)
        self.entry_client_email = Entry(self, width=40)

     
        self.entry_client_name.grid(row=0, column=1,padx=(0, 10), pady=(10, 10))
        self.entry_client_nickname.grid(row=1, column=1,padx=(0, 10), pady=(10, 10))
        self.entry_client_email.grid(row=2, column=1,padx=(0, 10), pady=(10, 10))

        self.label_resultaat = Label(self, width=40, anchor='w')

       
        # self.entry_wegdek.grid(row=2, column=1, sticky=E + W)
        # self.cbo_wegdek = Combobox(self, state="readonly", width=40)
        # self.cbo_wegdek['values'] = choices
        # self.cbo_wegdek.grid(row=2, column=1, sticky=E + W)

        #Label(self, text="km/u").grid(row=0, column=2)
        # Label(self, text="m/s").grid(row=0, column=2)
        # Label(self, text="sec", pady=10).grid(row=1, column=2)

        self.button_login = Button(
            self, text="Login", command=self.login_client)
        self.button_login.grid(row=3, column=0, columnspan=3, pady=(
            0, 5), padx=(5, 5), sticky=N + S + E + W)

        # root.protocol("WM_DELETE_WINDOW", _delete_window)


        self.master.title("Client login form")
        self.master.geometry("350x150")
        self.master.resizable(False, False)
#         self.master.mainloop()
     
        #Initial login window
     

  # client to server message
            # io_stream_server = socket_to_server.makefile(mode='rw')
            # io_stream_server.write(f"{client_name}\n")
            # io_stream_server.flush()
            # io_stream_server.write(f"{client_nickname}\n")
            # io_stream_server.flush()
            # io_stream_server.write(f"{client_email}\n")
            # io_stream_server.flush()

     #functies in init_window
        
          #Log out as client
        # def log_out_client():
        #     messagebox.askyesno("Log out", "Log out as client?")



        # #Tabs
        #  #TABS
        # my_tabs = ttk.Notebook(self.master)
        # my_tabs.pack(pady=15)

        # tab1 = Frame(my_tabs,width=500,height=500)
        # tab1.pack(fill='both', expand=1)
        # tab2 = Frame(my_tabs,width=500,height=500 )
        # tab2.pack(fill='both', expand=1)

        # tab3 = Frame(my_tabs,width=500,height=500 )
        # tab3.pack(fill='both', expand=1)

        # my_tabs.add(tab1, text='Tab1')
        # my_tabs.add(tab2, text='Tab2')
        # my_tabs.add(tab3, text='Tab3')


        # # Label frames
        # wrapper1 = LabelFrame(tab1, text="Clients List")
        # wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)

        # wrapper2 = LabelFrame(tab1, text="Get data by brand")
        # wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

        # wrapper3 = LabelFrame(tab1, text="Get amount of brands by calories per serving")
        # wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

        # wrapper4 = LabelFrame(tab1, text="Get amount of brands by rating")
        # wrapper4.pack(fill="both", expand="yes", padx=20, pady=10)

        # wrapper5 = LabelFrame(tab1, text="Get amount of brands by sodium")
        # wrapper5.pack(fill="both", expand="yes", padx=20, pady=10)

        # wrapper6 = LabelFrame(tab2, text="Read admin message")
        # wrapper6.pack(fill="both", expand="yes", padx=20, pady=10)

        # #log out client button
        # btn = Button(wrapper1, text="Log out", command=log_out_client)
        # btn.pack(side=tk.LEFT,padx=10 ,pady=0)

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

    def makeConnectionWithMysqlDatabase(self):
        try:
            logging.info("Making connection with MYSQL database...")
            mydb = mysql.connector.connect(
            host='localhost', user="root", passwd="root", database="thuisopdracht", auth_plugin="mysql_native_password")

            cursor = mydb.cursor()
            logging.info("Connected with MYSQL database")
        except Exception as ex:
            logging.error(f"Foutmelding connection with database: {ex}")

    def login_client(self):
        try:
            #Get client login input

            #client name
            client_name  = (self.entry_client_name.get())
            if client_name == "":
                messagebox.showerror("Name Invalid", "Name input can't be empty")   #client name error handling
                messagebox.ERROR("Empty name input error")

            #client name
            client_nickname = (self.entry_client_nickname.get())
            if client_nickname == "":
                messagebox.showerror("Nickname Invalid",
                             "Nickname input can't be empty")
                messagebox.ERROR("Empty nickname input error")

            client_email = (self.entry_client_email.get())
              # Email input error handling
            if client_email == "":
                messagebox.showerror("Email Invalid", "Email input can't be empty")
                messagebox.ERROR("Empty email input error")


            #Send client login input
            logging.info(f"Client logged in!")

            self.my_writer_obj.write(f"{ client_name }\n")
            logging.info(f"Client name: { client_name }")

             
           

            self.my_writer_obj.write(f"{ client_nickname}\n")
            logging.info(f"Client nickname: {client_nickname}")

            self.my_writer_obj.flush()

        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")
            messagebox.showinfo("Login error",
                                "Something has gone wrong...")

    def close_connection(self):
        try:
            logging.info("Close connection with server...")
            self.my_writer_obj.write("CLOSE\n")
            self.my_writer_obj.flush()
            self.socket_to_server.close()
        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")
            # messagebox.showinfo("Stopafstand berekenen",
            #                     "Something has gone wrong...")


logging.basicConfig(level=logging.INFO)

root = Tk()
# root.geometry("400x300")
app = Window(root)
root.mainloop()
