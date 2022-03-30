string = input()
string_list = list(string.upper()) #한글자씩 대문자로 저장.
string_element = list(set(string_list)) 
count_list = []

for i in string_element:
    cnt = string_list.count(i)
    count_list.append(cnt) #
    
if count_list.count(max(count_list)) > 1 :
    print('?')
else:
    max_number = count_list.index(max(count_list))
    print(string_element[max_number])
        




