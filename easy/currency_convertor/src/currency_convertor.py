import requests


def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    """This function retrieves the exchange rate for a given base currency and target currency.

    Args:
        base_currency (str): The base currency to convert from.
        target_currency (str): The target currency to convert to.

    Returns:
        float: The exchange rate for the given base and target currencies.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

def convert_currency(amount: float, exchange_rate: float) -> float:
    """This function converts an amount from one currency to another using an exchange rate.

    Args:
        amount (float): The amount to convert.
        exchange_rate (float): The exchange rate to use for the conversion.

    Returns:
        float: The converted amount.
    """
    return amount * exchange_rate

# if __name__ == '__main__':
#         base_currency = input("Enter the base currency: ")
#         target_currency = input("Enter the target currency: ")
#         amount = float(input("Enter the amount to convert: "))
#         exchange_rate = get_exchange_rate(base_currency, target_currency)
#         converted_amount = convert_currency(amount, exchange_rate)
#         print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")