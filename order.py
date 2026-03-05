def create_order(customer, item, discount=0):
    return f"{customer} ordered {item} with {discount}% discount"

if __name__ == "__main__":
    print(create_order("Alice", "Laptop"))

