class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = nums.count(num)

        buck = [[] for _ in range(len(nums) + 1)]

        for n , c in freq.items():
            buck[c].append(n)

        res = []
        for count in range(len(buck) - 1, 0, -1):
            for num in buck[count]:
                res.append(num)

                if len(res) == k:
                    return res

        return res