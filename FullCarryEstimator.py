import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

class CommodityFullCarryEstimator:
    def __init__(self):
        self.storage_costs_per_contract = {
            "lumber": 1000,
            "copper": 1000,
            "cocoa": 1000,
            "soybeans": 1000,
            "FCOJ": 1000,
            "cotton": 1000,
            "soybean oil": 1000,
            "wheat": 1000,
        }

        self.interest_rate = 0.05

        self.contract_expiration_date = {
            "lumber": self.get_contract_expiration_date("LBS"),
            "copper": self.get_contract_expiration_date("HG"),
            "cocoa": self.get_contract_expiration_date("CC"),
            "soybeans": self.get_contract_expiration_date("ZS"),
            "FCOJ": self.get_contract_expiration_date("OJ"),
            "cotton": self.get_contract_expiration_date("CT"),
            "soybean oil": self.get_contract_expiration_date("BO"),
            "wheat": self.get_contract_expiration_date("W"),
        }

        def get_contract_expiration_date(self, symbol):

            try:

                pass
            
            except Exception as e:
                print(f"Error getting contract expiration date for {symbol}: {e}")
                return None

        self.time_to_maturity = {
            "lumber": 1000,
            "copper": 1000,
            "cocoa": 1000,
            "soybeans": 1000,
            "FCOJ": 1000,
            "cotton": 1000,
            "soybean oil": 1000,
            "wheat": 1000,
        }

        self.spot_price = 100

        self.storage_cost_as_percentage_of_spot = self.storage_costs_per_contract / self.spot_price

    def calculate_full_carry(self, storage_costs_as_percentage_of_spot, interest_rate, time_to_maturity, spot_price):
        full_carry = spot_price * np.e ** (interest_rate + storage_cost_as_percentage_of_spot) * time_to_maturity
        return full_carry
 

