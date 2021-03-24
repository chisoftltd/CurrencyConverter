# Steps to Build the Python Project on Currency Converter
# Real-time Exchange rates
# Import required Libraries
# CurrencyConverter Class
# UI for CurrencyConverter
# Main Function

# Real-time Exchange rates
# Import the libraries
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Create the constructor of class
class CurrencyConverter():
    def __init__(self,url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

# Convert() method
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        #first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
    
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount

# And returns the converted amount
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)
print(converter.convert('SEK','NGN',100))