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

    # Check for invalid dtypes in quantity column
    if not all(type(value) is int for value in df["quantity"]):
        raise TypeError("Invalid data type in quantity column.")

    # Check if there are values equal or smaller than zero in quantity column
    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than zero.")

    # Restore quantity column to int type
    df["quantity"] = df["quantity"].astype(int)

    # Reset df index
    df = df.reset_index(drop=True)

    return df