import numpy as np

def clean_orders(df):
    # Create defensive copy
    df = df.copy()

    # Check for required columns
    required_columns = ["order_id", "customer_id", "quantity", "unit_price"]
    for col in required_columns:
        if col not in df.columns:
            raise KeyError("Missing required column(s)")
    
    # Drop rows with missing values in quantity and/or unit_price
    df = df.dropna(subset=["quantity", "unit_price"])

    # Check for missing values in order_id
    if df["order_id"].isna().any():
        raise ValueError("Invalid value(s) in order_id.")

    # Check for duplicated values in order_id
    if df["order_id"].duplicated().any():
        raise ValueError("Duplicated value(s) in order_id. This is not allowed.")

    # Check for missing values in customer_id
    if df["customer_id"].isna().any():
        raise ValueError("Invalid value(s) in customer_id.")

    # Check for invalid dtypes in quantity column
    if not all(type(value) is int for value in df["quantity"]):
        raise TypeError("Invalid data type in quantity column.")

    # Check if there are values equal or smaller than zero in quantity column
    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than zero.")

    # Restore quantity column to int type
    df["quantity"] = df["quantity"].astype("int64")

    # Check for invalid dtypes in unit_price column
    if not all(type(value) is int or type(value) is float for value in df["unit_price"]):
        raise TypeError("Invalid data type in unit_price column.")

    # Check for invalid values in unit_price column
    if any(
        value < 0 or
        not np.isfinite(value)
        for value in df["unit_price"]
    ):
        raise ValueError("Invalid value in unit_price column.")

    # Reset df index
    df = df.reset_index(drop=True)

    return df