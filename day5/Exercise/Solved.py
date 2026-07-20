def withdraw(balance: float, amount: float) -> float:
    """
    Withdraws a specified amount from a given balance.

    Args:
        balance (float): The current balance.
        amount (float): The amount to withdraw.

    Returns:
        float: The updated balance after the withdrawal.
    """
    if not isinstance(balance, (int, float)):
        raise TypeError("Balance should be a number")
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount should be a number")
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero")
    if amount > balance:
        raise ValueError("Insufficient funds for withdrawal")
    balance = balance - amount
    return balance
