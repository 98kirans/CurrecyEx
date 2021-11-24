import requests
from tkinter import *
class cc():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'EUR' : 
            amount = amount / self.currencies[from_currency] 
        amount = round(amount * self.currencies[to_currency], 3) 
        return amount
date = 'latest'
url = 'http://api.exchangeratesapi.io/v1/'+date+'?access_key=cd56b14c086000d5df3890edb0dbc71b&format=1'
converter = cc(url)
amount = 1
x = converter.convert('BTC','USD',amount)
print(x)
