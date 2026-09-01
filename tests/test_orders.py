from src.orders import calculate_order_revenue
import pandas as pd

def test_calculate_order_revenue():
    test_df = pd.DataFrame(
        {
            "order_id": [101, 102, 103],
            "quantity": [2, 3, 1],
            "unit_price": [10.00, 5.00, 20.00]
        }
    )
    df = calculate_order_revenue(test_df)
    expected_df = pd.DataFrame(
        {
            "order_id": [101, 102, 103],
            "quantity": [2, 3, 1],
            "unit_price": [10.00, 5.00, 20.00],
            "revenue": [20.00, 15.00, 20.00]
        }
    )
    pd.testing.assert_frame_equal(df, expected_df)

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