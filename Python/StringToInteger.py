class Solution:
    @staticmethod
    def my_atoi(self, s: str) -> int:
        if s == "" or s.isalpha():
            return 0
        if s.isnumeric():  # 只有正数才为 True
            result = int(s)
            if result > pow(2, 31):
                return 2147483647
            else:
                return result
        s = s.strip()  # 去除首尾空格
        sign = 0  # 0:不符合/中断   1:出现空格   2:下标为0/出现“+”“-”号   3:出现数字
        flag = False
        s0 = ""
        symbol = 1
        for i in range(len(s)):
            if s[i] == " ":
                sign = 1
                continue
            if (s[i] == "+" or s[i] == "-") and (sign == 1 or i == 0):

                if s[i] == "-":
                    symbol = -1
                sign = 2
                continue
            print(s0, sign, s[i], flag)
            if (i == 0 or sign == 2) and s[i].isnumeric():
                if flag is False and s[i] == "0" and i != 0:
                    continue
                else:
                    flag = True
                    sign = 2
                    s0 += s[i]
                    print(s[i])
            else:
                if flag:
                    break
                sign = 0
        print("s0:", s0)
        if s0.isnumeric():
            result = int(s0) * symbol
            if result < (-pow(2, 31)):
                return -2147483648
            if result > pow(2, 31):
                return 2147483647
            else:
                return result
        else:
            return 0


def main():
    example = Solution()
    s1 = "4193 with words"
    s2 = "4193"
    s3 = ""
    s4 = "-4"
    s5 = "   -4193"
    s6 = " ++++1"
    s7 = "words and 987"
    s8 = "3.14"
    s9 = "  -3.14"
    s10 = "  -+3.14"
    s11 = "words and -987"
    s12 = "-91283472332"
    print(example.my_atoi(s12))


if __name__ == "__main__":
    main()
