import pandas as pd

def calculate_order_revenue(df):
    required_cols = ["order_id", "quantity", "unit_price"]

    cols_in_df = df.columns

    for required_col in required_cols:
        if required_col not in cols_in_df:
            raise KeyError(f"Missing required column: {required_col}")

    df["revenue"] = df["quantity"] * df["unit_price"]
    return df