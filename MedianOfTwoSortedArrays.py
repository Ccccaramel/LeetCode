import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        v1 = 0
        v2 = 0
        half = (len1+len2)//2+(len1+len2)%2
        sign1 = 0
        sign2 = 0
        while sign1+sign2 <= half:
            v1 = v2
            if sign1+sign2 == len1+len2:
                break;
            elif sign2 == len2:
                v2 = nums1[sign1]
                sign1 += 1
            elif sign1 == len1:
                v2 = nums2[sign2]
                sign2 += 1
            elif nums1[sign1] <= nums2[sign2]:
                v2 = nums1[sign1]
                sign1 += 1
            else:
                v2 = nums2[sign2]
                sign2 += 1

        if (len1+len2) % 2:
            return v1
        else:
            return (v1+v2)/2

def main():
    example = Solution()
    list1 = [1, 3]
    list2 = [2]
    print(example.findMedianSortedArrays(list1, list2))


if __name__ == "__main__":
    main()
