from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import json
import requests

#colors
black = "#444466"
white = "#feffff"
blue = "#6f9fbd"
screen = "#0e0f13"
##

window = Tk()
window.title('')
window.geometry('350x350')
window.configure(background=screen)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_up = Frame(window, width=320, height=50, bg=black, pady=0, padx=0, relief='flat')
frame_up.grid(row=1, column=0)

frame_down = Frame(window, width=320, height=300, bg=screen, pady=0, padx=0, relief='flat')
frame_down.grid(row=2, column=0, sticky=NW)

def cryp():
    api_link ='https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,AOA,BRL'

    respon = requests.get(api_link)
    
    data = respon.json()
    
    # USD $ value
    value_usd = float(data['USD'])
    value_format_usd = "${:,.3f}".format(value_usd)
    c_usd['text'] = 'Dollars : $ '+value_format_usd
    
    # EUR $ value
    value_eur = float(data['EUR'])
    value_format_eur = "${:,.3f}".format(value_eur)
    c_eur['text'] = 'Euros : $ '+value_format_eur
    
    # BRL $ value
    value_brl = float(data['BRL'])
    value_format_brl = "${:,.3f}".format(value_brl)
    c_brl['text'] = 'Reais : $ '+value_format_brl
    
    frame_down.after(1000, cryp)

cryp()

window.mainloop()