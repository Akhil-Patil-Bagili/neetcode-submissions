class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output= [1] * len(nums)
        for i in range(len(output)):
            multiple = 1
            for j in range(len(nums)):
                if i!=j:
                    multiple *= nums[j]
            output[i] = multiple
        return output




        