class Solution:
        def removeElement(self, nums: List[int], val: int) -> int:
                left = 0
                right = len(nums) - 1

                while left <= right:
                    while left <= right and nums[left] != val:
                        left = left + 1

                    while left <= right and nums[right] == val:
                        right = right - 1

                    if left < right:
                        nums[left] = nums[right]
                        nums[right] = val
                        left = left + 1
                        right = right - 1
                return left