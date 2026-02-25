DATA = ["Apple", 2, 4.2]
X = Y = Z = None


def get_types():
    name, quantity, weight = DATA
    return type(name), type(quantity), type(weight)


def assign_globals():
    global X, Y, Z
    X, Y, Z = DATA[0], DATA[1], DATA[2]
