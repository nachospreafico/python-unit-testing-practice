import pandas as pd

def calculate_customer_retention(df, reference_date):
    # Create a defensive copy of the df
    df = df.copy()

    # Check df contains all required columns
    required_cols = ["order_id", "customer_id", "revenue", "order_date"]
    for col in required_cols:
        if col not in df.columns:
            raise KeyError("Missing required column(s).")

    # Convert reference_date to proper pandas datetime object
    reference_date = pd.to_datetime(reference_date, errors="coerce")

    # Check reference_date is a valid date
    if not isinstance(reference_date, pd.Timestamp):
        raise ValueError("Reference date is invalid")

    # Check reference_date is not in the future
    if reference_date.normalize() > pd.Timestamp.today().normalize():
        raise ValueError("Reference date is in the future")

    # Check order_id has no empty values
    if df["order_id"].isna().any():
        raise ValueError("Missing value(s) in order_id. This is not allowed.")

    # Check order_id has no duplicated values
    if df["order_id"].duplicated().any():
        raise ValueError("Duplicated value(s) in order_id. This is not allowed.")

    # Check if missing values in customer_id
    if df["customer_id"].isna().any():
        raise ValueError("Missing value(s) in customer_id. This is not allowed.")
    
    # Convert order_date to datetime object, coerce errors
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Check if errors in order_date
    if df["order_date"].isna().any():
        raise ValueError("Invalid date value(s) in order_date. This is not allowed.")
    
    # Check value types in revenue column
    if not all(
        type(revenue) is int or type(revenue) is float
        for revenue in df["revenue"]
    ):
        raise TypeError("Invalid type(s) in revenue. This is not allowed.")
    
    # Check if missing values in revenue
    if df["revenue"].isna().any():
        raise ValueError("Missing value(s) in revenue. This is not allowed.")
    
    # Check if negative values in revenue
    if (df["revenue"] < 0).any():
        raise ValueError("Negative value(s) in revenue. This is not allowed.")