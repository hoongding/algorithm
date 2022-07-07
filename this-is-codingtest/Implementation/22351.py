# 22351번 수학은 체육과목입니다 3
import sys
conti_num = input()
list(conti_num)

len_list = len(conti_num)


first_list = ''
second_list = ''
third_list = ''

first_digit_num = int(conti_num[0])
if len_list == 1:
    second_digit_num = int(str(00))
    third_digit_num = int(str(000))
    second_digit_num1 = int(str(00))
    third_digit_num1 = int(str(000))
elif len_list == 2:
    second_digit_num = int(str(conti_num[0])+str(conti_num[1]))
    second_digit_num1 = int(str(conti_num[0]) + str(conti_num[1]))
    third_digit_num = int(str(000))
    third_digit_num1 = int(str(000))
elif len_list >= 3:
    second_digit_num = int(str(conti_num[0]) + str(conti_num[1]))
    third_digit_num = int(str(conti_num[0])+str(conti_num[1])+str(conti_num[2]))
    second_digit_num1 = int(str(conti_num[0]) + str(conti_num[1]))
    third_digit_num1 = int(str(conti_num[0]) + str(conti_num[1]) + str(conti_num[2]))

first_digit_num1 = int(conti_num[0])

while len_list > len(first_list):
    first_list += str(first_digit_num)
    first_digit_num += 1
while len_list > len(second_list):
    second_list += str(second_digit_num)
    second_digit_num += 1
while len_list > len(third_list):
    third_list += str(third_digit_num)
    third_digit_num += 1

if first_list == conti_num:
    print(first_digit_num1, first_digit_num-1)
elif second_list == conti_num:
    print(second_digit_num1, second_digit_num-1)
else:
    print(third_digit_num1, third_digit_num-1)