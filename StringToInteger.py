import re

class Solution:
    def myAtoi(self, str: str) -> int:
        if str == "" or str.isalpha():
            return 0
        if str.isnumeric():  # 只有正数才为 True
            result = int(str)
            if result > pow(2,31):
                return 2147483647
            else:
                return result
        str = str.strip()  # 去除首尾空格
        sign = 0  # 0:不符合/中断   1:出现空格   2:下标为0/出现“+”“-”号   3:出现数字
        flag = False
        s0 = ""
        symbol = 1
        for i in range(len(str)):
            if str[i] == " ":
                sign = 1
                continue
            if ( (str[i] == "+" or str[i] == "-") and (sign == 1 or i == 0 ) ):
                
                if str[i] == "-":
                    symbol = -1
                sign = 2
                continue
            print(s0, sign,str[i],flag)
            if (i == 0 or sign == 2) and str[i].isnumeric():
                if flag == False and str[i] == "0" and i != 0:
                    continue
                else:
                    flag = True
                    sign = 2
                    s0 += str[i]
                    print(str[i])
            else:
                if flag == True:
                    break
                sign = 0
        print("s0:", s0)
        if s0.isnumeric():
            result = int(s0)*symbol
            if result < (-pow(2,31)):
                return -2147483648
            if result > pow(2,31):
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
    print(example.myAtoi(s12))
    
# if __name__ == "__main__":
main()
