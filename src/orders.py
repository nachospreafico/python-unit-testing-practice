import pandas as pd
import numpy as np

def calculate_order_revenue(df):
    # Check required columns exist in the df
    required_cols = ["order_id", "quantity", "unit_price"]

    cols_in_df = df.columns

    for required_col in required_cols:
        if required_col not in cols_in_df:
            raise KeyError(f"Missing required column: {required_col}")

    # Check if there are NaNs in quantity and unit_price columns 
    cols_with_no_nans = ["quantity", "unit_price"]
    for col in cols_with_no_nans:
        if df[col].isna().any():
            raise ValueError(f"Missing one or more values on column {col}")

    # Calculate the revenue column
    df["revenue"] = df["quantity"] * df["unit_price"]

    return df