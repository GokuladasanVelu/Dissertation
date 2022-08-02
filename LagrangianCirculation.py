def lagrangian_circulation(y, b, gammao, np, dy, elseif=None):
    circulation = []

    # Elliptic Loading -Trailing Horse Shoe circulation
    # for i in y:
    #     c = (gammao * i * (1 - ((2 * i) / b) ** 2) ** (-1 / 2)) * dy
    #     circulation.append(c)
    # return circulation

    # Fuselage/Flap-Wing -Trailing Horse Shoe circulation
    for i in y:
        if i <= 0.3:
            a1 = -44.4447
            a2 = 20.0001
            a3 = 0
            a4 = 1.4
            c = (-1*(3*a1*(i**2)) - 1*(2*a2*i) - a3) * dy
            circulation.append(c)
        elif i >= 0.3 and i <= 0.7:
            b1 = 1
            b2 = -2.725375
            b3 = 1
            b4 = 1.91828375
            c = (-1*(3*b1*(i**2)) - 1*(2*b2*i) - b3) * dy
            circulation.append(c)
        elif i >= 0.7 and i <= 1:
            c = (gammao * i * (1 - ((2 * i) / b) ** 2) ** (-1 / 2)) * dy
            circulation.append(c)

    return circulation
