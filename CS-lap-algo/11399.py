people = int(input())
person_time = list(map(int, input().split()))

sort_person_time = person_time.sort()

total_time = 0
add_time = 0
for time in person_time:
    add_time += time
    total_time += add_time

print(total_time)
