yimport random

def random_fun():
    # Random number tricks
    num = random.randint(1, 100)
    print(f"Random number: {num}")
    print(f"Is it even? {num % 2 == 0}")
    print(f"Squared: {num ** 2}")

    # Random list operations
    items = random.sample(range(1, 50), 10)
    print(f"\nRandom list: {items}")
    print(f"Max: {max(items)}, Min: {min(items)}")
    print(f"Sorted: {sorted(items)}")

    # Random string
    import string
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(chars, k=12))
    print(f"\nRandom password: {password}")

  edited by manish----

random_fun()
