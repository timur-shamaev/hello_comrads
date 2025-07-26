def compare_lists(list1, list2, ignore_case=False):
   if ignore_case:
       list2 = [item.lower() for item in list2]
       return [item for item in list1 if item.lower() not in list2]
   else:
       return [item for item in list1 if item not in list2]