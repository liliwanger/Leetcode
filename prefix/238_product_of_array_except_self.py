class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. 先计算前缀积：res[i] 存储 nums[i] 左侧所有元素的乘积
        # 此时 res[0] 保持 1，因为左边没东西
        length = len(nums)
        res = [1] *length

        for i in range(1, length):
            res[i]  = res[i-1] * nums[i-1]

        # 2. 再计算后缀积：动态维护一个右侧积变量 R
        # res[i] = 原有的前缀积 * 右侧所有积
        R=1
        for i in range(length-1, -1, -1):
            res[i] *= R
            R = R * nums[i]

        return res
