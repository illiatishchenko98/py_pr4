def dict_to_list(dict_to_convert):
    list_for_convertion = []
    for k, v in dict_to_convert.items():
        if type(v) == int:
            v *= 2
        list_for_convertion.append((k, v))
    return list_for_convertion


print(dict_to_list({'a': 24, 'b': 'abc', 'c': 12}))


# def abc(a, b):
#     q = []
#     for qa in a:
#         if type(qa) == b:
#             qa *= 2
#             q.append(qa)
#     return q


# print(abc([24, 'abc', True, 100], int))


def filter_list(list_to_filter, value_type):
    filtered_list = []
    for element in list_to_filter:
        if type(element) == value_type:
            filtered_list.append(element)
    return filtered_list


print(filter_list([35, True, 'abc', 10, 11, 11.1], int))
print(filter_list([35, True, 'abc', 10, 11, 11.1], str))


def filter_list(list_to_filter, value_type):
    return filter
