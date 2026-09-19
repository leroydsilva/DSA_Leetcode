class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0
        n=len(nums)
        i=0
        j=i+1
        while j < n:
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i +1



         