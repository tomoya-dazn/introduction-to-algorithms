def select_items(prices, weight, limit):
    unit_prices = {}
    for i, (price, weight) in enumerate(zip(prices, weights)):
        unit_price = price / weight
        unit_prices[i] = unit_price

    orderd_unit_prices = sorted(
        unit_prices.items(), key=lambda x: x[1], reverse=True)

    rest = limit
    items = {}
    for idx, _ in orderd_unit_prices:
        weight_to_steal = weights[idx] if weights[idx] <= rest else rest
        items[idx] = weight_to_steal

        rest -= weight_to_steal
        if rest <= 0:
            break

    return items


if __name__ == '__main__':
    prices = [100, 120, 60]
    weights = [20, 30, 10]

    print("  i |", end='')
    for i in range(len(prices)):
        print(f"{i:>3}|", end='')
    print('')
    print("p[i]|", end='')
    for price in prices:
        print(f"{price:>3}|", end='')
    print('')
    print("w[i]|", end='')
    for weight in weights:
        print(f"{weight:>3}|", end='')
    print('')

    items = select_items(prices, weight, 50)

    print("--- result ---")
    total_price = 0
    for idx, weight in items.items():
        price = prices[idx] / weights[idx] * weight
        print(f"item {idx} / weight = {weight} / price = {price}")

        total_price += price

    print(f"total = {total_price}")
