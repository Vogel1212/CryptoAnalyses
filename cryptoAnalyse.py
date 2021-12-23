from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image 

import requests
import json

fontWhite = "#feffff"
gray = "#b45f06"
screen = "#070709"

window  = Tk()
window.title('')
window.geometry('320x350')
window.configure(background=screen)


#frames
ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_up = Frame(window, width=320, height=50, bg=fontWhite, pady=0, padx=0, relief='flat')
frame_up.grid(row=1, column=0)

frame_down = Frame(window, width=320, height=300, bg=screen, pady=0, padx=0, relief='flat')
frame_down.grid(row=2, column=0, sticky=NW)


#fuction data api
#Info API Bitcoin
def infoBitcoin():
    apiCryp ='https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,AOA,BRL'

    respon = requests.get(apiCryp)

    data = respon.json()
    
    # value in USD
    vlue_usd = float(data['USD'])
    vlueFormatusd = "{:,.3f}".format(vlue_usd)
    c_usd['text'] = 'Dollars : USD '+vlueFormatusd
    
    # value in EURO
    vlue_euro = float(data['EUR'])
    vlueFormateur = "{:,.3f}".format(vlue_euro)
    c_euro['text'] = 'Euro : € '+vlueFormateur
    
    # value in BRL
    vlue_reais = float(data['BRL'])
    vlueFormatbrl = "{:,.3f}".format(vlue_reais)
    c_reais['text'] = 'Reais : R$ '+vlueFormatbrl
    
    
    frame_down.after(1000, infoBitcoin)


image = Image.open('images/coin.png')
image = image.resize((30,30), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

c_icon = Label(frame_up, image=image, compound=LEFT, bg=fontWhite,relief=FLAT )
c_icon.place(x=10, y=10)

c_name = Label(frame_up, text='Crypto Current Price', bg=fontWhite,fg=gray, relief=FLAT , anchor='center', font=('Arial 20'))
c_name.place(x=50, y=5)

c_usd = Label(frame_down, text='', bg=screen,fg=fontWhite, relief=FLAT , anchor='center', font=('Arial 12'))
c_usd.place(x=10, y=130)

c_euro = Label(frame_down, text='', bg=screen,fg=fontWhite, relief=FLAT , anchor='center', font=('Arial 12'))
c_euro.place(x=10, y=160)

c_reais = Label(frame_down, text='', bg=screen,fg=fontWhite, relief=FLAT , anchor='center', font=('Arial 12'))
c_reais.place(x=10, y=190)


infoBitcoin()

#Info API Bitcoin
def infoEthereum(args):
    
    apiCrypEt =''

    respon = requests.get(apiCrypEt)

    data = respon.json()
    
    # value in USD
    vlue_usdEt = float(data['USD'])
    vlueFormatusdEt = "{:,.3f}".format(vlue_usdEt)
    c_usdEt['text'] = 'Dollars : USD '+vlueFormatusdEt
    
    # value in EURO
    vlue_euroEt = float(data['EUR'])
    vlueFormateurEt = "{:,.3f}".format(vlue_euroEt)
    c_euroEt['text'] = 'Euro : € '+vlueFormateurEt
    
    # value in BRL
    vlue_reaisEt = float(data['BRL'])
    vlueFormatbrlEt = "{:,.3f}".format(vlue_reaisEt)
    c_reaisEt['text'] = 'Reais : R$ '+vlueFormatbrlEt
    
    
    frame_down.after(1000, infoEthereum)

c_usdEt = Label(frame_down, text='', bg=screen,fg=fontWhite, relief=FLAT , anchor='center', font=('Arial 12'))
c_usdEt.place(x=10, y=130)

c_euroEt = Label(frame_down, text='', bg=screen,fg=fontWhite, relief=FLAT , anchor='center', font=('Arial 12'))
c_euroEt.place(x=10, y=160)

c_reaisEt = Label(frame_down, text='', bg=screen,fg=fontWhite, relief=FLAT , anchor='center', font=('Arial 12'))
c_reaisEt.place(x=10, y=190)
    
infoEthereum()
    

window.mainloop()