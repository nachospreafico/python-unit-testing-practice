from unittest.mock import patch
from src.customer_status import get_customer_status
import pytest

def test_get_customer_status_return_standard():
    with patch("src.customer_status.fetch_customer_from_database") as mock_fetch:
        mock_fetch.return_value = {
            "customer_id": 123,
            "total_spent": 800
        }
        result = get_customer_status(123)
        mock_fetch.assert_called_once_with(123)
    assert result == "STANDARD"

def test_get_customer_status_returns_vip_with_1000():
    with patch("src.customer_status.fetch_customer_from_database") as mock_fetch:
        mock_fetch.return_value = {
            "customer_id": 123,
            "total_spent": 1000
        }
        result = get_customer_status(123)
        mock_fetch.assert_called_once_with(123)
    assert result == "VIP"

def test_get_customer_status_returns_vip():
    with patch("src.customer_status.fetch_customer_from_database") as mock_fetch:
        mock_fetch.return_value = {
            "customer_id": 123,
            "total_spent": 1200
        }
        result = get_customer_status(123)
        mock_fetch.assert_called_once_with(123)
    assert result == "VIP"

def test_get_customer_status_raises_exceptio():
    with patch("src.customer_status.fetch_customer_from_database") as mock_fetch:
        mock_fetch.side_effect = ConnectionError("Database unavailable")
        with pytest.raises(ConnectionError) as exc_info:
            get_customer_status(123)
        assert str(exc_info.value) == "Database unavailable"