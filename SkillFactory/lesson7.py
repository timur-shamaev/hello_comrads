def calculate_average(*args):
    if not args:
        return 0

    total = sum(args)
    count = len(args)
    average = total / count

    return round(average, 16)


print(calculate_average(1, 2, 3, 4, 5, -1))