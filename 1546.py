subject_num = int(input())

subject_score = list(map(int, input().split()))

max_score = max(subject_score)

for j in range(subject_num):
    subject_score[j] = subject_score[j]/max_score*100

score_add = 0
for k in range(subject_num):
    score_add = score_add + subject_score[k]

avg = score_add/subject_num

print(avg)

