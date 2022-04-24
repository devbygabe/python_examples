def output_greeting(name, returning_user=True):
    """output welcome text with provided name."""
    if returning_user:
        message = f"Welcome back, {name}!"
    else:
        message = f"Welcome, {name}!"

    print(message)


output_greeting("Leto", False)
output_greeting("Finn")
output_greeting("Indy", False)
output_greeting("Chloe")
