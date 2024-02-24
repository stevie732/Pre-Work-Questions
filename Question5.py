def is_consecutive(a_list):
    a_list.sort()
    for i in range(1, len(a_list)):
        if a_list[i] - a_list[i - 1] != 1:
         return False
    else:
         return True       
a_list = [1, 2, 3, 4, 5]
print(is_consecutive(a_list))
b_list = [1, 2, 3, 5, 6]
print(is_consecutive(b_list))