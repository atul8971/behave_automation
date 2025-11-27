def greet(name):
    """
    A simple function that greets a person by name.

    Args:
        name (str): The name of the person to greet

    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to Python."


def add_numbers(a, b):
    """
    Adds two numbers together.

    Args:
        a (int/float): First number
        b (int/float): Second number

    Returns:
        int/float: Sum of a and b
    """
    return a + b


if __name__ == "__main__":
    # Example usage
    print(greet("World"))
    print(f"5 + 3 = {add_numbers(5, 3)}")
