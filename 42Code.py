def calculate_total(price,tax=0.18):
    return price + (price * tax)

print(calculate_total(100,0.10))
