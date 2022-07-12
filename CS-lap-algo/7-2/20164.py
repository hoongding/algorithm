number_input = input()

number_list = list(number_input)
count_num = 0
all_case = []


def is_odd(num):
    num = int(num)
    if num % 2 == 1:
        return 1
    else:
        return 0


def cal_num(number, count):
    if len(number) == 1:
        all_case.append(count)
        return
    elif len(number) == 2:
        this_case = int(number[0]) + int(number[1])
        this_case_list = list(str(this_case))
        odd_num = 0
        for i in range(len(this_case_list)):
            odd_num += is_odd(this_case_list[i])
        cal_num(str(this_case), count+odd_num)
    else:
        for i in range(1, len(number)):
            for j in range(i + 1, len(number)):
                part1 = number[:i]
                part2 = number[i:j]
                part3 = number[j:]
                this_num = int(part1) + int(part2) + int(part3)
                this_case_list = list(str(this_num))
                odd_num = 0
                for k in range(len(this_case_list)):
                    odd_num += is_odd(this_case_list[k])
                cal_num(str(this_num), count+odd_num)


for n in range(len(number_list)):
    count_num += is_odd(number_list[n])
cal_num(number_input, count_num)
print(min(all_case), max(all_case))
