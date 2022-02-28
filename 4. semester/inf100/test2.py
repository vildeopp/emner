from decimal import Decimal
class NoPrice(Exception):
    pass
class NotEnoughPaid(Exception):
    pass
def cash_register_events(cash_register_filename):
    """Read cash register events from file and store
    in two dictionaries and a variable"""
    purchases = {}
    returns = {}
    payment = 0
    with open(cash_register_filename, encoding="utf8") as cash_register_file:
        for line in cash_register_file:
            event, value = line.rstrip().split(sep=";")
            if event == "buy":
                purchases[value] = purchases[value] + 1 if value in purchases else 1
            elif event == "return":
                returns[value] = returns[value] + 1 if value in returns else 1
            elif event == "pay":
                payment += Decimal(value)
    return (purchases, returns, payment)
def prices(prices_filename):
    """Read product prices from file and store in dictionary."""
    prices = {}
    with open(prices_filename, encoding="utf8") as prices_file:
        for line in prices_file:
            item, price = line.split(sep=";")
            prices.update({item: Decimal(price)})
    return prices
def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""
    price_dict = prices(prices_filename)
    purchases, returns, payment = cash_register_events(cash_register_filename)
    total = 0
    purchases_returns = []
    for item, number in sorted(purchases.items()):
        if item not in price_dict:
            raise NoPrice
        cost = number * price_dict[item]
        total += cost
        purchases_returns.append((number, item, cost))
    for item, number in sorted(returns.items()):
        if item not in price_dict:
            raise NoPrice
        cost = number * price_dict[item]
        total -= cost
        purchases_returns.append((-number, item, -cost))
    vat = total * Decimal("0.2")
    if payment < total:
        raise NotEnoughPaid
    change = total - payment
    return (purchases_returns, total, vat, payment, change)
def receipt(prices_filename, cash_register_filename):
    """Construct a receipt of the cash register events,
    given the store prices."""
    # get receipt content from receipt_content()
    purcases_returns, total, vat, payment, change = receipt_content(
        prices_filename, cash_register_filename
    )
    # the formatted lines of the receipt
    receipt_lines = [f"{'Nr.':>4}  {'Item':18}  {'Price':>10}"]
    for nr, item, price in purcases_returns:
        receipt_lines.append(f"{nr:4d}  {item:18}  {price:10.2f}")
    receipt_lines.append(f"Total: {total}")
    receipt_lines.append(f"Of which VAT: {vat:.2f}")
    receipt_lines.append(f"Payment: {payment}")
    receipt_lines.append(f"Change {change}")
    # add some dividers
    max_len = max(len(line) for line in receipt_lines)
    divider = "-" * max_len
    receipt_lines.insert(1, divider)
    receipt_lines.insert(-4, divider)
    receipt_lines.insert(-2, divider)
    return "\n".join(receipt_lines)
if __name__ == "__main__":
    print(receipt("uke_11/prices.txt", "uke_11/cash_register.txt"))