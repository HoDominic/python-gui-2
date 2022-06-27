# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
from doctest import master
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
import pickle
import pandas as pd
from matplotlib import pyplot as plt

class LoginWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # Functies oproepen!
        self.init_window()
        self.makeConnnectionWithServer()


    # Creation of init_window
    def init_window(self):
        

        self.pack(fill=BOTH, expand=1)

        Label(self, text="Client Name:", padx=10, pady=10).grid(row=0)
        Label(self, text="Client Nickname:", pady=10).grid(row=1)
        Label(self, text="Client Email:", pady=10).grid(row=2)
      

        self.entry_client_name = Entry(self, width=40)
        self.entry_client_nickname = Entry(self, width=40)
        self.entry_client_email = Entry(self, width=40)

     
        self.entry_client_name.grid(row=0, column=1,padx=(0, 10), pady=(10, 10))
        self.entry_client_nickname.grid(row=1, column=1,padx=(0, 10), pady=(10, 10))
        self.entry_client_email.grid(row=2, column=1,padx=(0, 10), pady=(10, 10))

        self.button_login = Button(
            self, text="Login", command=self.login_client)
        self.button_login.grid(row=3, column=0, columnspan=3, pady=(
            0, 5), padx=(5, 5), sticky=N + S + E + W)

        # root.protocol("WM_DELETE_WINDOW", _delete_window)

        #Initial window layout
        self.master.title("Client login form")
        self.master.geometry("350x150")
        self.master.resizable(False, False)
        #self.master.mainloop()



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

         # self.label = Label(master, text ="This is the main window")
        # self.label.pack(master,side = TOP, pady = 10)

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

    def login_client(self):
        try:

            mydb = mysql.connector.connect(
            host='localhost', user="root", passwd="root", database="thuisopdracht", auth_plugin="mysql_native_password")
            cursor = mydb.cursor()


            #Get client login input

              # Id voor DB
            client_id = cursor.lastrowid

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


               # Id has to be sent!
            sql = "INSERT INTO clients VALUES(%s,%s,%s,%s)"
            cursor.execute(sql, (client_id, client_name,
                                client_nickname, client_email))

            #must be commited after executing query
            mydb.commit()
            print("Logged in as client!")
            messagebox.showinfo('Login', "Logged in!")


            #Send client login input
            logging.info(f"Client logged in!")

            self.my_writer_obj.write(f"{ client_name }\n")
            logging.info(f"Client name: { client_name }")

             
            self.my_writer_obj.write(f"{ client_nickname}\n")
            logging.info(f"Client nickname: {client_nickname}")

            self.my_writer_obj.write(f"{ client_email}\n")
            logging.info(f"Client email: {client_email}")
            self.my_writer_obj.flush()
            self.master.destroy()
            #New_Window.new_client_window(self)
            ClientWindow.new_client_window(self)
            
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

  


 

class ClientWindow(LoginWindow):
    def __init__(self, master=None):
        #Frame.__init__(self, master)
        super().__init__(master = master)
        self.master = master
        self.new_client_window()        







    def new_client_window(self):
       
        self.master = Tk()
        self.master.geometry("500x500")
        self.master.title("Client GUI")



        def log_out_client():
            messagebox.askyesno("Log out", "Log out as client?")
            mydb = mysql.connector.connect(
            host='localhost', user="root", passwd="root", database="thuisopdracht", auth_plugin="mysql_native_password")
            cursor = mydb.cursor()

            #delete most recent Id in DB
            query = "DELETE FROM thuisopdracht.clients ORDER BY id desc limit 1"
            cursor.execute(query)
            mydb.commit()
            
            print("Logged out as client!")
            messagebox.showinfo('Log out', "Logged out!")

        #Chart threads
        def get_calories_data_thread():
            get_calories_data_thread = threading.Thread(target=get_calories_data)
            get_calories_data_thread.start()
            time.sleep(1)

        def get_rating_data_thread():
            get_rating_data_thread = threading.Thread(target=get_rating_data)
            get_rating_data_thread.start() 

        def get_sodium_data_thread():
            get_sodium_data_thread = threading.Thread(target=get_sodium_data)
            get_sodium_data_thread.start() 

        def get_calories_with_params_thread():
            get_calories_with_params_thread = threading.Thread(target=get_calories_with_params)
            get_calories_with_params_thread.start()   

        def get_ratings_with_params_thread():
            get_ratings_with_params_thread = threading.Thread(target=get_ratings_with_params)
            get_ratings_with_params_thread.start()

        def get_sodium_with_params_thread():
            get_sodium_with_params_thread = threading.Thread(target=get_sodium_with_params)
            get_sodium_with_params_thread.start()

        def read_admin_message_thread():
            read_admin_message_thread = threading.Thread(target=read_admin_message)
            read_admin_message_thread.start()
        
        #Client GUI tabs
        my_tabs = ttk.Notebook(self.master)
        my_tabs.pack(pady=15)

        self.tab1 = Frame(my_tabs,width=500,height=500)
        self.tab1.pack(fill='both', expand=1)
        self.tab2 = Frame(my_tabs,width=500,height=500 )
        self.tab2.pack(fill='both', expand=1)

        self.tab3 = Frame(my_tabs,width=500,height=500 )
        self.tab3.pack(fill='both', expand=1)

        my_tabs.add(self.tab1, text='Tab1')
        my_tabs.add(self.tab2, text='Tab2')
        my_tabs.add(self.tab3, text='Tab3')
    

  
         # Label frames
        self.wrapper1 = LabelFrame(self.tab1, text="Clients List")
        self.wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)

        self.wrapper2 = LabelFrame(self.tab1, text="Get data by brand")
        self.wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

        self.wrapper3 = LabelFrame(self.tab1, text="Get amount of brands by calories per serving")
        self.wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

        self.wrapper4 = LabelFrame(self.tab1, text="Get amount of brands by rating")
        self.wrapper4.pack(fill="both", expand="yes", padx=20, pady=10)

        self.wrapper5 = LabelFrame(self.tab1, text="Get amount of brands by sodium")
        self.wrapper5.pack(fill="both", expand="yes", padx=20, pady=10)

        self.wrapper6 = LabelFrame(self.tab2, text="Read admin message")
        self.wrapper6.pack(fill="both", expand="yes", padx=20, pady=10)

         #log out client button
        self.btn = Button(self.wrapper1, text="Log out", command=log_out_client)
        self.btn.pack(side=tk.LEFT,padx=10 ,pady=0)

        #get calories by chart button
        self.btn = Button(self.wrapper2, text="Calories by brand", command=get_calories_data_thread)
        self.btn.pack(side=tk.LEFT,padx=10 ,pady=0)

        self.btn = Button(self.wrapper2, text="Rating by brand", command=get_rating_data_thread)
        self.btn.pack(side=tk.LEFT,padx=20 ,pady=0)

        self.btn = Button(self.wrapper2, text="Sodium by brand", command=get_sodium_data_thread)
        self.btn.pack(side=tk.LEFT,padx=30 ,pady=0)

        



        self.input_calories = Label(self.wrapper3, text='input minvalue calories')
        self.input_calories.pack(side=tk.LEFT, padx=10)
        self.entry_client = Entry(self.wrapper3)
        self.entry_client.pack(side=tk.LEFT, padx=10)

        self.btn = Button(self.wrapper3, text="Get data", command=get_calories_with_params_thread)
        self.btn.pack(side=tk.LEFT,padx=20 ,pady=0)


        #WRAPPER4
        self.input_rating = Label(self.wrapper4, text='input minvalue rating')
        self.input_rating.pack(side=tk.LEFT, padx=10)
        self.entry_client2 = Entry(self.wrapper4)
        self.entry_client2.pack(side=tk.LEFT, padx=10)

        self.btn = Button(self.wrapper4, text="Get data", command=get_ratings_with_params_thread)
        self.btn.pack(side=tk.LEFT,padx=20 ,pady=0)

        #WRAPPER5
        self.input_rating = Label(self.wrapper5, text='input minvalue sodium')
        self.input_rating.pack(side=tk.LEFT, padx=10)
        self.entry_client3 = Entry(self.wrapper5)
        self.entry_client3.pack(side=tk.LEFT, padx=10)

        self.btn = Button(self.wrapper5, text="Get data", command=get_sodium_with_params_thread)
        self.btn.pack(side=tk.LEFT,padx=20 ,pady=0)


        #WRAPPER6
        self.btn = Button(self.wrapper6, text="Read admin message", command=read_admin_message_thread)
        self.btn.pack(side=tk.LEFT,padx=20 ,pady=0)


        
       


            #Get pickle data from txt files
        def get_calories_data():
            txt_data_file = open(r'C:\Users\domin\OneDrive\Bureaublad\python-gui-2\dataset\cereals_data.txt', 'rb')
            txt_data = pickle.load(txt_data_file)

            #get dataframe (pickled)data from client
            #protein data
            calories_column = txt_data['calories']
            calories_column = sorted(txt_data['calories'])
            #brands data
            brands_column = txt_data['name']
            brands_column = sorted(txt_data['name'])
        
            txt_data_file.close()


            #*CHART CALORIES BY CEREAL BRAND
            #chart size
            chart_figure = plt.figure(figsize=(30,30))
            
            #label font size
            plt.rcParams.update({'font.size': 6})
            
            #configure x and y for chart
            chart_x =  calories_column
            chart_y =  brands_column

            #sort list by value!
            sorted_chartx = sorted(chart_x,key=int)
            sorted_charty = sorted(chart_y,key=str)
            logging.info(sorted_chartx)
            logging.info(sorted_charty)

            #?Set x-axis
            #plt.xticks([0, 10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160])

            bar_width = [0.4]
            plt.barh(sorted_charty,sorted_chartx,height=bar_width )

            font1 = {'family':'serif','color':'blue','size':14}
            font1_title = {'family':'serif','color':'blue','size':20}

            plt.xlabel('calories',fontdict = font1)
            plt.ylabel('brand',fontdict = font1)
            plt.title('calories by brand (per serving)',fontdict = font1_title)

            plt.show()


        def get_rating_data():
            txt_data_file = open(r'C:\Users\domin\OneDrive\Bureaublad\MCT2\semester2\Advanced_programming_maths\2022-labooplossingen-HoDominic\project-2022-HoDominic\cereals_data.txt', 'rb')
            txt_data = pickle.load(txt_data_file)

            #get dataframe (pickled)data from client
            #protein data
            calories_column = txt_data['rating']
            calories_column = sorted(txt_data['rating'])
            #brands data
            brands_column = txt_data['name']
            brands_column = sorted(txt_data['name'])
        
            txt_data_file.close()


            #*CHART CALORIES BY CEREAL BRAND
            #chart size
            chart_figure = plt.figure(figsize=(30,30))
            
            #label font size
            plt.rcParams.update({'font.size': 6})
            
            #configure x and y for chart
            chart_x =  calories_column
            chart_y =  brands_column

            

            #sort list by value!
            sorted_chartx = sorted(chart_x,key=float)
            sorted_charty = sorted(chart_y,key=str)
            logging.info(sorted_chartx)
            logging.info(sorted_charty)

            #?Set x-axis
            plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
            plt.xlim([0, 100])

            bar_width = [0.4]
            plt.barh(chart_y,chart_x,height=bar_width )

            font1 = {'family':'serif','color':'blue','size':14}
            font1_title = {'family':'serif','color':'blue','size':20}

            plt.xlabel('Rating',fontdict = font1)
            plt.ylabel('Brand',fontdict = font1)
            plt.title('Rating by brand',fontdict = font1_title)

            plt.show()


        def get_sodium_data():
            txt_data_file = open(r'C:\Users\domin\OneDrive\Bureaublad\MCT2\semester2\Advanced_programming_maths\2022-labooplossingen-HoDominic\project-2022-HoDominic\cereals_data.txt', 'rb')
            txt_data = pickle.load(txt_data_file)

            #get dataframe (pickled)data from client
            #sodium data
            sodium_column = txt_data['sodium']
            sodium_column = sorted(txt_data['sodium'])
            #brands data
            brands_column = txt_data['name']
            brands_column = sorted(txt_data['name'])
        
            txt_data_file.close()


            #*CHART CALORIES BY CEREAL BRAND
            #chart size
            chart_figure = plt.figure(figsize=(30,30))
            
            #label font size
            plt.rcParams.update({'font.size': 6})
            
            #configure x and y for chart
            chart_x =  sodium_column
            chart_y =  brands_column

            

            #sort list by value!
            sorted_chartx = sorted(chart_x,key=float)
            sorted_charty = sorted(chart_y,key=str)
            logging.info(sorted_chartx)
            logging.info(sorted_charty)

            bar_width = [0.4]
            plt.barh(sorted_charty,sorted_chartx,height=bar_width )

            font1 = {'family':'serif','color':'blue','size':14}
            font1_title = {'family':'serif','color':'blue','size':20}

            plt.xlabel('Sodium',fontdict = font1)
            plt.ylabel('Brand',fontdict = font1)
            plt.title('Sodium by brand',fontdict = font1_title)

            plt.show()


        def get_calories_with_params():
        
            global input_param

            #get client entry value as int
            input_param =  int(self.entry_client.get())
            print(input_param)
                

            txt_data_file = open(r'C:\Users\domin\OneDrive\Bureaublad\MCT2\semester2\Advanced_programming_maths\2022-labooplossingen-HoDominic\project-2022-HoDominic\cereals_data.txt', 'rb')
            txt_data = pickle.load(txt_data_file)

            #get dataframe (pickled)data from client
            #calories data
            calories_column = txt_data['calories']
            calories_column = sorted(txt_data['calories'])
            print(calories_column)
    
            #bins data
            bins_column=  bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]
            bins_column = sorted(bins)

            #print(calories_column)
            #turn list of str in list of int
            calories_column_int = [int(values) for values in calories_column]
        

            #condition calories list with input parameter
            calories_column_with_param = [i for i in calories_column_int if i >= input_param]
            
                
            #sort
            sorted_calories_column_with_param = sorted(calories_column_with_param)
            print(sorted_calories_column_with_param)

                

            #*CHART CALORIES BY CEREAL BRAND WITH PARAMETER
            #chart size
        
            plt.figure(figsize=(30,30))
                
            #label font size
            plt.rcParams.update({'font.size': 6})
                
            #configure x and y for chart
            chart_x =  sorted_calories_column_with_param
            chart_y =  bins_column

            print(chart_x)
            print(chart_y)



            plt.hist(chart_x,chart_y)
        
        

            font1 = {'family':'serif','color':'blue','size':14}
            font1_title = {'family':'serif','color':'blue','size':20}

            plt.xlabel('Calories',fontdict = font1)
            plt.ylabel('Amount of cereal brands',fontdict = font1)
            plt.title(f'Cereals with minimum {input_param} calories (per serving) ',fontdict = font1_title)

            plt.show()


        def get_ratings_with_params():
            global input_param_rating

            #get client entry value as int
            input_param_rating =  int(self.entry_client2.get())
            print(input_param_rating)
    
            txt_data_file = open(r'C:\Users\domin\OneDrive\Bureaublad\MCT2\semester2\Advanced_programming_maths\2022-labooplossingen-HoDominic\project-2022-HoDominic\cereals_data.txt', 'rb')
            txt_data = pickle.load(txt_data_file)

            #get dataframe (pickled)data from client
            #calories data
            ratings_column = txt_data['rating']
            ratings_column = sorted(txt_data['rating'])
            print(ratings_column)
        

            #bins data
            bins_column=  bins = [0,10,20,30,40,50,60,70,80,90,100]
            bins_column = sorted(bins)

    
            #turn list of str in list of int
            ratings_column_int = [float(values) for values in ratings_column]
            #print(calories_column_int)

            #condition calories list with input parameter
            ratings_column_with_param = [i for i in ratings_column_int if i >= input_param_rating]
        
                
            #sort
            sorted_ratings_column_with_param = sorted(ratings_column_with_param)
            print(sorted_ratings_column_with_param)

                

            #*CHART CALORIES BY CEREAL BRAND WITH PARAMETER
            #chart size
        
            plt.figure(figsize=(30,30))
                
            #label font size
            plt.rcParams.update({'font.size': 6})
                
            #configure x and y for chart
            chart_x =  sorted_ratings_column_with_param
            chart_y =  bins_column

            print(chart_x)
            print(chart_y)



            plt.hist(chart_x,chart_y)
        
        

            font1 = {'family':'serif','color':'blue','size':14}
            font1_title = {'family':'serif','color':'blue','size':20}

            plt.xlabel('Rating',fontdict = font1)
            plt.ylabel('Amount of cereal brands',fontdict = font1)
            plt.title(f'Cereals with minimum rating of {input_param_rating} ',fontdict = font1_title)

            plt.show()
            
        def get_sodium_with_params():
            global input_param_sodium

            #get client entry value as int
            input_param_sodium =  int(self.entry_client3.get())
            print(input_param_sodium)
    
            txt_data_file = open(r'C:\Users\domin\OneDrive\Bureaublad\MCT2\semester2\Advanced_programming_maths\2022-labooplossingen-HoDominic\project-2022-HoDominic\cereals_data.txt', 'rb')
            txt_data = pickle.load(txt_data_file)

            #get dataframe (pickled)data from client
            #sodium data
            sodium_column = txt_data['sodium']
            sodium_column = sorted(txt_data['sodium'])
            print(sodium_column)
        

            #bins data
            bins_column=  bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330]
            bins_column = sorted(bins)


            #turn list of str in list of int
            sodium_column_int = [int(values) for values in sodium_column]
        

            #condition calories list with input parameter
            sodium_column_with_param = [i for i in sodium_column_int if i >= input_param_sodium]
            #print(calories_column_with_param)
                
            #sort
            sorted_sodium_column_with_param = sorted(sodium_column_with_param)
            print(sorted_sodium_column_with_param)

            

            #*CHART CALORIES BY CEREAL BRAND WITH PARAMETER
            #chart size
        
            plt.figure(figsize=(30,30))
                
            #label font size
            plt.rcParams.update({'font.size': 6})
                
            #configure x and y for chart
            chart_x =  sorted_sodium_column_with_param
            chart_y =  bins_column

            print(chart_x)
            print(chart_y)



            plt.hist(chart_x,chart_y)
        
        

            font1 = {'family':'serif','color':'blue','size':14}
            font1_title = {'family':'serif','color':'blue','size':20}

            plt.xlabel('Sodium',fontdict = font1)
            plt.ylabel('Amount of cereal brands',fontdict = font1)
            plt.title(f'Cereals with minimum sodium amount of {input_param_sodium} ',fontdict = font1_title)

            plt.show()


      



    def __del__(self):
        self.close_connection()




       

    



   

    




#     def __init__(self, master=None):
#         super().__init__(master = master)
   
#         self.init_window()



    # def init_window(self):
    #             self.title("New Window")
    #             self.geometry("200x200")
    #             label = Label(self, text ="This is a new Window")
    #             label.pack()

# creates a Tk() object

# def new_window():
#     master = Tk()
#     master.geometry("200x200")
    
#     label = Label(master, text ="This is the main window")
#     label.pack(side = TOP, pady = 10)
    
#     # a button widget which will
#     # open a new window on button click
#     btn = Button(master,
#                 text ="Click to open a new window")
    
#     # Following line will bind click event
#     # On any click left / right button
#     # of mouse a new window will be opened
#     btn.bind("<Button>",
#             lambda e: New_Window(master))
    
#     btn.pack(pady = 10)
    
# mainloop, runs infinitely



logging.basicConfig(level=logging.INFO)

root = Tk()
# root.geometry("400x300")
app = LoginWindow(root)
root.mainloop()
