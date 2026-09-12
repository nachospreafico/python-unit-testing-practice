import pandas as pd

def calculate_customer_metrics(df):
    if "revenue" not in df.columns.to_list():
            raise KeyError("Missing required column: revenue")
    if df["order_id"].duplicated().any():
        raise ValueError("Duplicated values in order_id, this is not allowed.")
    if (df["revenue"] < 0).any():
        raise ValueError("Negative value(s) in revenue column. This is not allowed.")
    if df["revenue"].isna().any():
        raise ValueError("Missing value(s) in revenue, this is not allowed.")
    output = df.groupby("customer_id", as_index=False)[["order_id", "revenue"]].agg(
            total_orders=("order_id", "count"),
            total_revenue=("revenue", "sum"),
            average_order_value=("revenue", "mean")
    ).reset_index(drop=True)
    return output