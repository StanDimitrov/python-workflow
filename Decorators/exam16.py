#
# my_str = 'hello2020'
# list_pos = []
#
# for i, value in enumerate(my_str):
#     print('Intex: i', i, 'Value: value', value)
my_str = 'hello2020'
count_list = [0,0,0,0,0,0,0,0,0,0]

count_list = [0 for x in range(10)]
for k in my_str:
    if k.isdigit():
        count_list[int(k)] += 1
print(count_list)