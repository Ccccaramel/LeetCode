from operator import eq
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t_nums = nums.copy()
        t_nums.sort()  # 排序
        l = len(t_nums)  # 列表长度
        left = 0
        right = l-1
        value = target//2  # 获取和的一半,理想情况下在 t_nums 此元素的位置离 key1 与 key2 距离相等
        key = right//2  # key 在 key1 与 key2 中间,以下简称 中间key
        while 1:  # 搜索 中间key 所在位置
            if t_nums[key] >= value:
                right = key
            elif t_nums[key] < value:
                left = key
            if left+1 >= right:
                # print(left,right)
                key = left
                if t_nums[right] == value:
                    key = right
                if t_nums[left] == value:
                    key = left
                # print(left)
                break
            key = (left + right)//2

        # print(key,t_nums[key],value)  # 中间key 实际值 期望值
        # 找到了一个中间 key
        key1 = key
        key2 = key+1
        # print("key1:", key1, ",key2:", key2)
        dic = {}
        while 1:
            value1 = t_nums[key1]
            d_value = target-t_nums[key1]
            while 1:
                # print(key1,key2,dic,d_value)
                value2 = t_nums[key2]
                # print(value2)
                if d_value in dic:
                    place1 = nums.index(value1)
                    if value1 == d_value:
                        place2 = nums.index(d_value,place1+1)
                    else:
                        place2 = nums.index(d_value)
                    li = [place1, place2]
                    li.sort()
                    del t_nums, dic, right, left, value, value1, value2, key, key1, key2, place1, place2
                    return li
                dic[value2] = key2
                if value2 > d_value:  #不存在
                    break
                if value2 == d_value:  #找到了!
                    place1 = nums.index(value1)
                    if value1 == value2:
                        place2 = nums.index(value2,place1+1)
                    else:
                        place2 = nums.index(value2)
                    li = [place1, place2]
                    li.sort()
                    return li
                key2 += 1
                if key2 >=l:  # 超出列表长度
                    break
            key1 -= 1
            if key1 < 0:
                break



def twoSum(nums: List[int], target: int) -> List[int]:
    print(twoSum.__annotations__)
    pass

def main():
    sol = Solution()
    lis = [2, 7, 11, 15]
    su = 9
    # twoSum(lis, su)  取消注释看看 -> 到底是什么
    print(sol.twoSum(lis, su))