n = int(input())
nums=[]
for i in range(n):
    a=int(input())
    nums.append(a)

if len(nums)>3:
    nums.sort()
    firstFour =1
    for i in range(4):
        firstFour = firstFour * nums[i]
    lastFour = 1
    for i in range(len(nums)-4,len(nums)):
        lastFour = lastFour * nums[i]
    fl = 1
    for i in range(2):
        fl = fl*nums[i]
    for i in range(len(nums)-2,len(nums)):
        fl = fl*nums[i]
    res = float(max([lastFour,firstFour,fl]))
    print(res)
else:
    print('Invalid Input')