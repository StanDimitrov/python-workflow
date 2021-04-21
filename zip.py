my_str = [0,1,2,3,4,5,6,7,8,9] #== [1,2,0,0,0,0,0,1,0,2]
#
# 0 = 1
# 1 = 2
# 7 = 1
# 9 = 2
# others = 0
#
# test = input(my_str)

count_list = [0,0,0,0,0,0,0,0,0,0] # You will use this list for holding the count for each digit you find in the string my_str

for i in my_str:
    if i.isdigit():
        if i == 0:
            count_list[0] += 1
        elif i == 1:
            count_list[1] += 1
        elif i == 2:
            count_list[2] += 1
        elif i == 3:
            count_list[3] += 1
        elif i == 4:
            count_list[4] += 1
        elif i == 5:
            count_list[5] += 1
        elif i == 6:
            count_list[6] += 1
        elif i == 7:
            count_list[7] += 1
        elif i == 8:
            count_list[8] += 1
        else:
            count_list[9] += 1
    print(count_list)