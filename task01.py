def pyramid(levels: int = 5, symbol: str = '*'):
    """
    Prints pyramid pattern with the specified number of levels and symbol

    Args:
        levels (int): The number of levels in the pyramid. Default is 5
        symbol (str): The symbol used to construct the pyramid. Default is '*'

    Returns:
        None
    """
    for i in range(levels):
        spaces = ' ' * (levels - i - 1)
        symbols = symbol * (2 * i + 1)
        print(spaces + symbols)


pyramid(5)