def lagrangian_circulation(y, b, gammao, np, dy, elseif=None):
    circulation = []

    # Trailing Horse Shoe circulation
    for i in y:
        c = (gammao * i * (1 - ((2 * i) / b) ** 2) ** (-1 / 2)) * dy
        circulation.append(c)
    return circulation

    # Elliptic Loading
    # for i in y:
    #     c = (1 - (i ** 2)) ** (1/2)
    #     circulation.append(c)
    # return circulation

    #Fuselage/Flap-Wing
    # for i in y:
    #     if i <= 0.3:
    #         a1 = 1
    #         a2 = 2
    #         a3 = 3
    #         a4 = 4
    #         c = (a1*(i**3)) + (a2*(i**2)) + (a3 * i) + (a4 * i)
    #         circulation.append(c)
    #     elif i >= 0.3 and i <= 0.7:
    #         b2 = 2
    #         b3 = 3
    #         b4 = 4
    #         b1 = 1
    #         c = (b1*(i**3)) + (b2*(i**2)) + (b3 * i) + (b4 * i)
    #         circulation.append(c)
    #     elif i >= 0.7 and i <= 1:
    #         c = (1 - (i ** 2)) ** (1 / 2)
    #         circulation.append(c)
    #
    # return circulation
