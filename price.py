def final_price(price, tax_rate=0.1):
    if price < 0 or tax_rate < 0:
        raise ValueError("price and tax_rate must not be negative")
    else:
        return round(price * (1 + tax_rate), 2)
