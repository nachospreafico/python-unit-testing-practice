import pandas as pd

def calculate_order_revenue(df):
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df