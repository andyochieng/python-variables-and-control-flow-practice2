def print_even_keys(input_dict):
    for key, value in input_dict.items():
        if value % 2 == 0:
            print(f"{key} is even")
    return "Function running"
print(print_even_keys({"a": 1, "b": 2, "c": 3}))