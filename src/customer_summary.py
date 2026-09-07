import pandas as pd

def get_customer_summary(df, min_revenue):
    if df["order_id"].duplicated().any():
        raise ValueError("Duplicated values in order_id, this is not allowed.")
    grouped_df = df.groupby("customer_id", as_index=False).agg(
        total_orders=("order_id", "size"),
        total_revenue=("revenue", "sum")
    )
    filtered_grouped_df = grouped_df[grouped_df["total_revenue"] >= min_revenue]
    filtered_grouped_df = filtered_grouped_df.reset_index(drop=True)
    return filtered_grouped_df