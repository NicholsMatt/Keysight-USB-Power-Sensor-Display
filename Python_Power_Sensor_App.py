import pyvisa
import webbrowser
import random

import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
import tkinter
from tkinter import filedialog



################################
#  START FUNCTION DEFINITIONS  #
################################

#A hilarous waste of time in the help menu
def wtf():
    list = [0, 1, 2, 3]
    wtf = random.choice(list)
    if wtf == 0: #rick roll
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    elif wtf == 1: #mii song
        webbrowser.open('https://www.youtube.com/watch?v=po-0n1BKW2w')
    elif wtf == 2: #thomas had never seen such BS before...
        webbrowser.open('https://i.kym-cdn.com/entries/icons/original/000/031/008/thumb.png')
    elif wtf == 3: #xkcd schematic
        webbrowser.open('https://xkcd.com/730/')
    else: #default to rick roll
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                
#Launches the documentation/github page
def launchdocumentation():
    webbrowser.open('https://github.com/NicholsMatt/Keysight-USB-Power-Sensor-Display')

#Save data to file
def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
#still needs completed

def graph():
    house_prices = np.random.normal(0, 30, 5000)
    plt.hist(house_prices, 500)
    plt.show()

##############################
#  END FUNCTION DEFINITIONS  #
##############################

list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
disp = random.choice(list2)

#root window
root = Tk()
root.geometry('640x480')
root.title('USB Power Sensor Display')

#menu bar
menubar = Menu(root)
root.config(menu=menubar)

#'File' menu
filemenu = Menu(menubar, tearoff=False, selectcolor='red')
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Save Data', command=file_save)
    #Add submenu
submenu = Menu(filemenu, tearoff=False, selectcolor='red')
submenu.add_checkbutton(label='Display Graph')
submenu.add_checkbutton(label='BIG TEXT')
submenu.add_command(label='Measurement Config')
submenu.add_command(label='Data Capture Config')
filemenu.add_cascade(label='Preferences', menu=submenu)
    #Finish 'File' menu
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.destroy)

#'VISA' menu
visamenu = Menu(menubar, tearoff=False, selectcolor='red')
menubar.add_cascade(label='VISA Config', menu=visamenu)
visamenu.add_command(label='USB VISA Config')
visamenu.add_command(label='*IDN?')

#'Help' menu
helpmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='¯\_(ツ)_/¯', command=wtf)
helpmenu.add_command(label='About', command=launchdocumentation)

my_button = Button(root, text="Graph it", command=graph)
my_button.pack()

start_button = Button(root, text="Start")
stop_button = Button(root, text="Stop")
start_button.pack()
stop_button.pack()

powerData = np.random.normal(0, 30, 1)
powerDataDisp = Label(root, text=powerData)
powerDataDisp.pack()

root.after(10)
powerDataDisp.update()



root.mainloop() 





# rm = pyvisa.ResourceManager()
# rm.list_resources()

#USB0::0x2A8D::0xA518::MY57430002::0::INSTR
#Keysight U8485A Power Meter VISA address