def sort(nums):

#numbers changed

    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [2,4,1,3,6,5]
sort(nums)
print(nums)