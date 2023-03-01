# def edit_distance(source_string: str, target_string: str):
#     source_dict = {}
#     target_dict = {}
#     operation_required = 0
#     set_dict_from_string(source_string, source_dict)
#     set_dict_from_string(target_string, target_dict)
#     i = 0
#     while i < len(source_string):
#         source_element = source_string[i]
#         target_element = target_string[i]
#         count_source_element = source_dict[source_element]
#         count_target_element = target_dict[target_element]
#         if target_element == source_element:
#
#
#
# def set_dict_from_string(string_value: str, dict_value: {}):
#     for i in range(0, len(string_value)):
#         element = string_value[i]
#         if element in dict_value:
#             dict_value[element] = dict_value[element] + 1
#         else:
#             dict_value[element] = 1
