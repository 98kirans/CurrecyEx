import requests
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import datetime

class cc():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'EUR' : 
            amount = amount / self.currencies[from_currency] 
        amount = round(amount * self.currencies[to_currency], 2) 
        return amount
    	
root = Tk()

intro = Label(root, text=" REAL TIME CURRENCY CONVERTER").pack()

from_currency_label = Label(root, text = "Enter From Currency").pack()
from_currency_variable = StringVar()
from_currency_variable = Entry(root)
from_currency_variable.pack()

to_currency_label = Label(root, text = "Enter To Currency").pack()
to_currency_variable = StringVar()
to_currency_variable = Entry(root)
to_currency_variable.pack()

amount_label = Label(root, text = "Enter Amount").pack()
amount_field = Entry(root)
amount_field.pack()

date_label = Label(root, text = "Enter Date(YYYY-MM-DD) or latest").pack()
date_box = StringVar()
date_box = Entry(root)
date_box.pack()




def perf():
	from_curr = from_currency_variable.get()
	to_curr = to_currency_variable.get()
	amt = float(amount_field.get())

	date = date_box.get()
	url = 'http://api.exchangeratesapi.io/v1/'+date+'?access_key=cd56b14c086000d5df3890edb0dbc71b&format=1'
	converter = cc(url)
	converted_amount = converter.convert(from_curr,to_curr,amt)
	converted_amount_field.delete(0, END)
	converted_amount_field.insert(0, converted_amount)
	

convert_button = Button(root, text = "Convert", fg = "teal", command = perf).pack()
converted_amount_field_label = Label(root, text = 'Converted Amount').pack()
converted_amount_field = Entry(root)
converted_amount_field.pack()

lb3 = Label(root, text = date_box.get()).pack()




root.mainloop()