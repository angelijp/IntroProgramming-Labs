for i in range(20):
    print(i)

num_list = list(range(2, 22))

even_nums = []

for x in num_list:
        if x % 2 == 0:
            even_nums.append(x)

print(even_nums)
