def max_num_in_list(lst):
    max_num = lst[0]
    for a in lst:
        if a > max_num:
            max_num = a
    return max_num

print(max_num_in_list([1, 2, -8, 0]))
