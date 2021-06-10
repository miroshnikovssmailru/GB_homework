my_list = [1, 'text', 1.2, True, None, (1 + 1j), ({1, 2})]
for i, item in enumerate(my_list):
    print(f"{i} {item} - {type(item)}")
