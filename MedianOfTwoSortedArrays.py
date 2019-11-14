import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        nums = (nums1+nums2)
        nums.sort()
        """
        nums = sorted(nums1+nums2)  # sorted() 比 sort() 更快,详见Python/package191009/test17.py
        print(nums)
        l = len(nums)
        if l%2:
            return nums[l//2]
        else:
            return (nums[int(l/2)-1]+nums[int(l/2)])/2

def main():
    example = Solution()
    list1 = [1, 3, 5]
    list2 = [2, 4, 5, 6]
    print(example.findMedianSortedArrays(list1, list2))


if __name__ == "__main__":
    main()
