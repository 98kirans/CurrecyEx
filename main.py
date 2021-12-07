
import requests
from tkinter import *
from tkinter import ttk
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
root.geometry("400x400")
def perf():
	global amt, from_curr, to_curr
	from_curr = from_currency_dropdown.get()
	to_curr = to_currency_dropdown.get()
	amt = float(amount_field.get())

	date = date_box.get()
	url = 'http://api.exchangeratesapi.io/v1/'+date+'?access_key=cd56b14c086000d5df3890edb0dbc71b&format=1'
	converter = cc(url)
	converted_amount = converter.convert(from_curr,to_curr,amt)
	converted_amount_field.delete(0, END)
	converted_amount_field.insert(0, str(converted_amount) + ' ' + str(to_curr))

root.title('Real Time Currency Ex Converter')
intro = Label(root, text=" REAL TIME CURRENCY CONVERTER").pack()

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=cd56b14c086000d5df3890edb0dbc71b&format=1'
converter = cc(url)

from_currency_label = Label(root, text = "Select From Currency").pack()
from_currency_dropdown =ttk.Combobox(root ,values=list(converter.currencies.keys()), width = 12)
from_currency_dropdown.pack()

to_currency_label = Label(root, text = "Select To Currency").pack()
to_currency_dropdown =ttk.Combobox(root,values=list(converter.currencies.keys()), width = 12)
to_currency_dropdown.pack()

amount_label = Label(root, text = "Enter Amount").pack()
amount_field = Entry(root, width = 15)
amount_field.pack()

date_label = Label(root, text = "Enter Date(YYYY-MM-DD) or latest").pack()
date_box = StringVar()
date_box = Entry(root, width = 15)
date_box.pack()




root.mainloop()
