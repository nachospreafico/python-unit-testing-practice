from src.orders import calculate_order_revenue
from src.customer_summary import get_customer_summary
import pandas as pd

def build_customer_report(df, min_revenue):
    df = calculate_order_revenue(df)
    summary = get_customer_summary(df, min_revenue)
    return summary