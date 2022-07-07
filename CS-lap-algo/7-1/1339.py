# 1339번 단어수학
word_num = int(input())
word_list = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_list = list(alphabet)
alphabet_weight = [0]*26
result = 0
for __ in range(0, word_num):
    word_list.append(input())

for word in word_list:
    current_word = list(word)
    current_len = len(word)
    i = 0
    for current_alphabet in current_word:
        current_index = alphabet_list.index(current_alphabet)
        power_num = current_len - i - 1
        alphabet_weight[current_index] += 10 ** power_num
        i += 1

alphabet_weight.sort(reverse=True)

for i in range(0, 10):
    result += alphabet_weight[i] * (9 - i)


print(result)