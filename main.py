
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
