

class Sum:

    def __init__(self):
        pass

    def sum_indices(self, values):
        result = 0
        for value in values:
            result += value
        return result

    def sum_ordered(self, values):
        result = 0
        for value in sorted(values):
            result += value
        return result


