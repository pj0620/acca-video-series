def accelerated(t, f0, f1):
    return ((f1 - f0) / (f1 + f0)) * (t ** 2) + ((2 * f0) / (f0 + f1)) * t
