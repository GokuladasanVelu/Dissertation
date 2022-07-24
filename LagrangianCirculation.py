def lagrangian_circulation(y, b, gammao, np, dy):
    circulation = []
    # Trailing Horse Shoe circulation
    # for i in y:
    #     c = (gammao * i * (1 - ((2 * i) / b) ** 2) ** (-1 / 2)) * dy
    #     circulation.append(c)
    # return circulation

    # Elliptic Loading
    for i in y:
        c = (1 - (i ** 2)) ** (1/2)
        circulation.append(c)
    return circulation

