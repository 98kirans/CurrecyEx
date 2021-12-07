
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