import requests
import pandas as pd
import json
import csv
import io
from tkinter import *
import tkinter as tk
#---- constants-------------------------------#
API_KEY = "K1AXX01WY0BSF8YV"
BASE_URL = "https://www.alphavantage.co/query"
FUNCTION_TIME_SERIES = "TIME_SERIES_INTRADAY"
SYMBOL = "eurusd"
INTERVAL = "5min"
TIME_PERIOD_SHORT = "20"
TIME_PERIOD_MEDIUM = "60"
TIME_PERIOD_LONG = "200"
OUTPUTSIZE = "full"
SERIES_TYPE = "open"
MONTH= "2024-11"

functions= ["TIME_SERIES_INTRADAY", "SMA", "EMA", "DEMA", "WMA", "TEMA", "TRIMA", "T3", "RSI", "STOCHRSI",
            "WILLR", "ADX", "ADXR", "CCI", "CMO", "TRIX", "ATR", "KAMA", "ROC", "ROCR", "AROON", "AROONOSC", "MFI",
            "NATR", "STOCH", "MACDEXT", "MAMA", "STOCHF", "APO", "PPO", "BOP", "ULTOSC", "OBV"]

def data_extract():
	for function in functions:
		function_name = function
		if function_name == "TIME_SERIES_INTRADAY":
			parameters = {
				"function":function_name,
				"symbol": SYMBOL,
				"interval": INTERVAL,
				"time_period": TIME_PERIOD_MEDIUM,
				"outputsize": OUTPUTSIZE,
				"series_type": SERIES_TYPE,
				"apikey":API_KEY,
				}
		elif function_name in ["SMA", "EMA", "DEMA", "WMA", "DEMA", "TEMA", "TRIMA","KAMA", "T3", "STOCHRSI", "RSI", "MOM",
		"CMO", "ROC", "ROCR", "AROON", "TRIX"]:
			parameters = {
				"function": function_name,
				"symbol": SYMBOL,
				"interval": INTERVAL,
				"time_period": TIME_PERIOD_MEDIUM,
				"month": MONTH,
				"series_type": SERIES_TYPE,
				"apikey": API_KEY,
			}
		elif function_name in ["MAMA", "MACDEXT","APO", "ADX", "ADXR", "WILLR", "PPO", "CCI", "AROONOSC", "MFI", "ATR", "NATR"]:
			parameters = {
				"function": function_name,
				"symbol": SYMBOL,
				"month": MONTH,
				"interval": INTERVAL,
				"series_type": "open",
				"apikey": API_KEY,
			}
		elif function_name in ["STOCH", "STOCHF", "BOP", "ULTOSC", "OBV"]:
			parameters = {
				"function": function_name,
				"symbol": SYMBOL,
				"month": MONTH,
				"interval": INTERVAL,
				"apikey": API_KEY,
			}

		response_intra_day = requests.get(BASE_URL, params=parameters)
		data = response_intra_day.json()
		with open(f"{SYMBOL}_{function_name}.json", 'w') as json_file:
			json.dump(data, json_file, indent=4)

		df = pd.read_json(f"{SYMBOL}_{function_name}.json")
		df.to_csv(f"{SYMBOL}_{function_name}_{MONTH}.csv", index=False)
		df.index.name = 'timestamp'
		df.reset_index(inplace=True)

		print(f"Downloaded {SYMBOL} data for {SYMBOL}")

data_extract()

