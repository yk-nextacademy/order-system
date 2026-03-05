def create_order(customer, item):
    return f"{customer} ordered {item}"

if __name__ == "__main__":
    print(create_order("Alice", "Laptop"))
