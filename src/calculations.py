def calculate_conversion_rate(conversions, visitors):
    if not isinstance(conversions, int):
        raise TypeError("Conversions must be a non-negative integer")

    if not isinstance(visitors, int):
            raise TypeError("Visitors must be a positive integer")
    
    if visitors <= 0:
        raise ValueError("Visitors must be greater than zero")

    if conversions < 0:
        raise ValueError("Conversions cannot be negative")

    if conversions > visitors:
        raise ValueError("Conversions cannot exceed visitors")

    return conversions / visitors