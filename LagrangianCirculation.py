def lagrangian_circulation(y, b, gammao, np, dy):
    circulation = []
#
    for i in y:
        c = (gammao * i * (1 - ((2 * i) / b) ** 2) ** (-1 / 2)) * dy
        circulation.append(c)
    return circulation
