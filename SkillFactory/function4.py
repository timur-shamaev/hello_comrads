def compare_lists(list1, list2, ignore_case=False):
    set2 = set()

    if ignore_case:
        set2 = {item.lower() for item in list2}
    else:
        set2 = set(list2)

    result = []
    for item in list1:
        if ignore_case:
            if item.lower() not in set2:
                result.append(item)
        else:
            if item not in set2:
                result.append(item)

    return result