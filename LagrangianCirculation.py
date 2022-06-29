def lagrangian_circulation(gammao, spanwisedistance, span):
    y = spanwisedistance
    b = span
    circulation = gammao*y*(1-((2*y)/b)**2)**(-1/2)

    return circulation