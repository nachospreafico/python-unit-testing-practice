import pandas as pd

def calculate_customer_retention(df, reference_date):
    # Create a defensive copy of the df
    df = df.copy()

    # Check df contains all required columns
    required_cols = ["order_id", "customer_id", "revenue", "order_date"]
    for col in required_cols:
        if col not in df.columns:
            raise KeyError("Missing required column(s).")

    # Check order_id has no empty values
    if df["order_id"].isna().any():
        raise ValueError("Missing value(s) in order_id. This is not allowed.")

    # Check order_id has no duplicated values
    if df["order_id"].duplicated().any():
        raise ValueError("Duplicated value(s) in order_id. This is not allowed.")

    # Check if missing values in customer_id
    if df["customer_id"].isna().any():
        raise ValueError("Missing value(s) in customer_id. This is not allowed.")