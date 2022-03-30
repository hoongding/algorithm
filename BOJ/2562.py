nums = []
for i in range(9):
    nums.append(int(input()))

index = 0
for i in range(9):
    if max(nums) == nums[i]:
        index = i
    
print(max(nums))
print(index+1)
