# 10814번 나이순 정렬
join_people = []
for i in range(int(input())):
    temp1, temp2 = input().split()
    join_people.append([int(temp1), i, temp2])

join_people.sort()

for i in range(len(join_people)):
    print(join_people[i][0], join_people[i][2])