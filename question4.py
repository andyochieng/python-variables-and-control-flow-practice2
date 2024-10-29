def reverse_list_strings(list_strings):
    list_reverse = []
    for i in list_strings:
        print(i)

        reversed_string = i[::-1]
        list_reverse.append(reversed_string)
    return list_reverse

print(reverse_list_strings(['apple', 'banana', 'cherry']))