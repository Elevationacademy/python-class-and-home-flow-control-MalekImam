def my_enumerate(object_en, start=0):
    for i in range(start, len(object_en)):
        yield i, object_en[i]


list_enum = [1, 2, 3, 4, 5]
print(list(my_enumerate(list_enum, 2)))
