import math
import time


class Solution:
    s = ""
    reasult = ""
    list0 = []

    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if length <= 1 or length <= numRows or numRows <= 1:
            return s
        self.s = s
        for i in range(numRows):  # 创建好容器
            self.list0.append([])
        width = 2 * (numRows - 1)  # (饱和状态下)纵向分区的字符数量
        units = math.ceil(length / width)  # 纵向分区的总数量
        for r0 in range(numRows):
            print("row:", r0)
            for v0 in range(units+1):
                spot = v0 * width  # 分支点
                print("spot:", spot,r0)
                if r0 == 0 or r0 + 1 == numRows:
                    if spot + r0 < length:
                        self.collapse(spot + r0)
                    continue
                # if 0 > spot-r0 or spot+r0<0 or spot-r0 >= length and spot+r0 >r0:
                #     continue
                if length > spot - r0 > 0:
                    self.collapse(spot - r0)
                if 0 < spot + r0 < length:
                    self.collapse(spot + r0)
        return self.reasult

    def collapse(self, spot: int):
        print(self.s[spot])
        self.reasult += self.s[spot]


def main():
    s = "PAYPALISHIRING"
    numRows = 3
    example = Solution()
    print(example.convert(s, numRows))


if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print(t2 - t1)
