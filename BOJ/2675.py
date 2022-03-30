test_num = int(input())
repeat_list = []
string_list = []

for i in range(test_num):
    repeat, string = input().split()
    repeat_list.append(repeat)
    string_list.append(string)

for i in range(test_num):
    print_string = ''
    for j in range(len(string_list[i])):
        print_string = print_string + list(string_list[i])[j]*int(repeat_list[i])
    print(print_string)