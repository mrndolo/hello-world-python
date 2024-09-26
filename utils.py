def find_max(number_list):
    max_no = number_list[0]
    for number in number_list:
        if number > max_no:
            max_no = number
    return max_no