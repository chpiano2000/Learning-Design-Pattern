def get_default_price(original_price: float) -> float:
    return original_price


def get_pre_order_price(original_price: float) -> float:
    return original_price * 0.8


def get_promotion_price(original_price: float) -> float:
    return original_price * 0.9 if original_price <= 200 else original_price - 30


get_price_mapper = {
    "default": get_default_price,
    "pre_order": get_pre_order_price,
    "promotion": get_promotion_price,
}


def get_price(original_price: float, promotion_type: str) -> float:
    return get_price_mapper[promotion_type](original_price)


print(get_price(200, "pre_order"))
