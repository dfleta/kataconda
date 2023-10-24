def loose_change(cents):

    coinKeys = ['Nickels', 'Pennies', 'Dimes', 'Quarters']
    coinValues = [5, 1, 10, 25]

    wallet = dict(zip(coinKeys, coinValues))

    coins = list(sorted(wallet.values()))

    change = []
    i = len(coins) - 1
    while cents > 0 and i >= 0:
        if cents >= coins[i]:
            cents = cents - coins[i]
            change.append(coins[i])
        else:
            i -= 1

    change_dict = dict.fromkeys(coinKeys, 0)
    for coin in change:
        for coinKeys in wallet:
            if wallet[coinKeys] == coin:
                change_dict[coinKeys] += 1

    return change_dict