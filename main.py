
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
root.geometry("400x500")

def perf():
    global amt, from_curr, to_curr1, to_curr2
    from_curr = from_currency_dropdown.get()
    to_curr1 = to_currency_dropdown1.get()
    to_curr2 = to_currency_dropdown2.get()
    amt = float(amount_field.get())

    date = date_box.get()
    url = 'http://api.exchangeratesapi.io/v1/'+date+'?access_key=cd56b14c086000d5df3890edb0dbc71b&format=1'
    converter = cc(url)
    converted_amount1 = converter.convert(from_curr,to_curr1,amt)
    converted_amount2 = converter.convert(from_curr,to_curr2,amt)
    converted_amount_field1.delete(0, END)
    converted_amount_field1.insert(0, str(converted_amount1) + ' ' + str(to_curr1))
    converted_amount_field2.delete(0, END)
    converted_amount_field2.insert(0, str(converted_amount2) + ' ' + str(to_curr2))

root.title('Real Time Currency Ex Converter')
intro = Label(root, text=" REAL TIME CURRENCY CONVERTER").pack()

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=cd56b14c086000d5df3890edb0dbc71b&format=1'
converter = cc(url)

from_currency_label = Label(root, text = "Select From Currency").pack()
from_currency_dropdown =ttk.Combobox(root ,values=list(converter.currencies.keys()), width = 12)
from_currency_dropdown.pack()

to_currency_label1 = Label(root, text = "Select First To Currency").pack()
to_currency_dropdown1 =ttk.Combobox(root,values=list(converter.currencies.keys()), width = 12)
to_currency_dropdown1.pack()

to_currency_label2 = Label(root, text = "Select Second To Currency").pack()
to_currency_dropdown2 =ttk.Combobox(root,values=list(converter.currencies.keys()), width = 12)
to_currency_dropdown2.pack()

amount_label = Label(root, text = "Enter Amount").pack()
amount_field = Entry(root, width = 15)
amount_field.pack()

date_label = Label(root, text = "Enter Date(YYYY-MM-DD) or latest").pack()
date_box = StringVar()
date_box = Entry(root, width = 15)
date_box.pack()

	
def display_chart1():
	get_yearly_rates(amt, from_curr, to_curr1, int(chart_field.get()))

def display_chart2():
    get_yearly_rates(1, from_curr, to_curr2, int(chart_field.get()))

convert_button = Button(root, text = "Convert", fg = "teal", command = perf).pack()

converted_amount_field1_label1 = Label(root, text = 'Converted Amount of First Currency').pack()
converted_amount_field1 = Entry(root, width = 15)
converted_amount_field1.pack()

converted_amount_field_label2 = Label(root, text = 'Converted Amount of Second Currency').pack()
converted_amount_field2 = Entry(root, width = 15)
converted_amount_field2.pack()

chart_label = Label(root, text = 'Enter No. of days to view chart comparison').pack()
chart_field = Entry(root, width = 5)
chart_field.pack()

chart_button1 = Button(root, text = "View Chart 1", fg = "teal", command = display_chart1).pack()
chart_button2 = Button(root, text = "View Chart 2", fg = "teal", command = display_chart2).pack()

def get_yearly_rates(amount, currency, converted_currency, amount_of_days) :
	today_date = datetime.datetime.now()
	date_1year = (today_date - datetime.timedelta(days=1 * amount_of_days))
	url2=f'https://api.exchangerate.host/timeseries'
	payload = {'base': currency, 'amount': amount, 'start_date': date_1year.date(), 'end_date': today_date.date()}

	response = requests.get(url2, params=payload)
	data = response.json()

	currency_history = {}
	rate_history_array = []

	for item in data['rates']:
		currency_date = item
		currency_rate = data['rates'][item][converted_currency]
		currency_history[currency_date] = [currency_rate]
		rate_history_array.append(currency_rate)

	pd_data = pd.DataFrame(currency_history).transpose()
	pd_data.columns = ['Rate']
	pd.set_option('display.max_rows', None)
	#print(pd_data)
	plt.plot(rate_history_array)
	plt.ylabel(f'{amount} {currency} to {converted_currency}')
	plt.xlabel('Days')
	plt.title(f' Current rate for {amount} {currency} to {converted_currency} is {rate_history_array[-1]}')
	plt.show()


root.mainloop()
