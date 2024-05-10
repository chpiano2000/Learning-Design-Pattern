def get_price(original_price: float, promotion_type: str = "default") -> float:
    if promotion_type == "pre_order":
        return original_price * 0.8

    if promotion_type == "promotion":
        return original_price * 0.9 if original_price <= 200 else original_price - 30

    if promotion_type == "black_friday":
        return original_price * 0.9 if original_price <= 200 else original_price - 50

    if promotion_type == "default":
        return original_price


print(get_price(200, "pre_order"))
