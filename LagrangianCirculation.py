def lagrangian_circulation(y, b, gammao, np):
    circulation=[]
#changed
    # for i in range(1, (np+1)):
    #     circulation[i] = gammao * y[i] * (1 - ((2 * y[i]) / b) ** 2) ** (-1 / 2)
    #
    # return circulation

    for i in y:
        c = gammao * i * (1 - ((2 * i) / b) ** 2) ** (-1 / 2)
        circulation.append(c)
    return circulation