#DZ3Collections 1
my_list = [1, 3, 1, 10, 3, 6, 7, 8, 5, 8, 22, 39, 10]
new_list = []
my_set = set(my_list)

for item in my_set:
    if my_list.count(item) > 1:
        new_list.append(item)

print(new_list)
