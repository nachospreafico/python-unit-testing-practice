from src.orders import calculate_order_revenue
import pandas as pd

test_df = pd.DataFrame(
    {
        "order_id": [101, 102, 103],
        "quantity": [2, 3, 1],
        "unit_price": [10.00, 5.00, 20.00]
    }
)

def test_calculate_order_revenue():
    df = calculate_order_revenue(test_df)
    assert "revenue" in df.columns.to_list()
    assert df["revenue"].to_list() == [20.0, 15.0, 20.0]
    assert df.shape[0] == 3
    assert df.shape[1] == 4
    assert df.iloc[:,:-1].columns.to_list() == ["order_id", "quantity", "unit_price"]
    assert df["order_id"].to_list() == [101, 102, 103]
    assert df["quantity"].to_list() == [2, 3, 1]
    assert df["unit_price"].to_list() == [10.00, 5.00, 20.00]

def test_empty_dataframe():
    empty_df = pd.DataFrame(
        {
            "order_id": [],
            "quantity": [],
            "unit_price": []
            }
        )
    df = calculate_order_revenue(empty_df)
    assert "revenue" in df.columns.to_list()
    assert df.shape[0] == 0
    assert df.shape[1] == 4
    assert df.iloc[:,:-1].columns.to_list() == ["order_id", "quantity", "unit_price"]