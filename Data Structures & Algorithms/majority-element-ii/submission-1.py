class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        threshold = len(nums)// 3
        res = []
        
        for num, count in counts.items():
            if count > threshold:
                res.append(num)
                
        return res