def clean_orders(df):
    # Create defensive copy
    df = df.copy()

    # Check for required columns
    required_columns = ["order_id", "customer_id", "quantity", "unit_price"]
    for col in required_columns:
        if col not in df.columns:
            raise KeyError("Missing required column(s)")