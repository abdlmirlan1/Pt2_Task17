def find(*nums):
    a = len(nums)
    total = (a+1)*(a+2)/2
    summ = sum(nums)
    print(nums, "Missing number is ", int(total - summ))
find(1,2,3,5,6)
find(1,3,4,5,6)