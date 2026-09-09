def fetch_customer_from_database(customer_id):
    raise NotImplementedError("Real database connection not implemented")


def get_customer_status(customer_id):
    customer = fetch_customer_from_database(customer_id)

    if customer["total_spent"] >= 1000:
        return "VIP"

    return "STANDARD"