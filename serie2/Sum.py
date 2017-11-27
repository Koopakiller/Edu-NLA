# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


def sum_indices(addends):
    """
    Sums the given addends, starting by the first number and following the list
    """
    result = 0
    for addend in addends:
        result += addend
    return result

def sum_ordered(addends):
    """
    Sums the given addends, starting by the smallest and following the natural order.
    """
    result = 0
    for addend in sorted(addends):
        result += addend
    return result

def sum_ordered_grouped_by_sign(addends):
    """
    Sums the given addends; All negative and all positive values are added separately
    and will be added together in the last step.
    """
    pos = 0
    neg = 0
    for addend in sorted(addends):
        if addend > 0:
            pos += addend
        if addend < 0:
            neg += addend
    return pos + neg