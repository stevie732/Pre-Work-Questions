# Question 3
def max_num_in_list(a_list):
    max_num = a_list[0]
    for x in a_list:
        if x > max_num:
            max_num = x
    return max_num

a_list = [1, 2, 3, 4, 5]
max_num = max_num_in_list(a_list)
print(max_num)
