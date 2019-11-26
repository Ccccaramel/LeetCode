import re


class Solution:
    def myAtoi(self, str: str) -> int:
        if str == "" or str.isalpha():
            return 0
        if str.isnumeric():
            return int(str)
        list0 = str.split(" ")
        for s in list0:
            if re.findall(r'\d+.\d+', s):
                value = int(s.split(".")[0])
            else:
                try:
                    value = int(s)
                except:
                    continue
            if -pow(2, 31) <= value <= pow(2, 31):
                return value
            else:
                return  -pow(2, 31)
        return 0



def main():
    example = Solution()
    s1 = "6 is my lucky number"
    s2 = "666"
    s3 = "words and 987"
    s4 = "-91283472332"
    s5 = "-4"
    s6 = "3.14159"
    s7 = "4193 with words"
    s8 = ".3"
    s9 = " ++++"
    s10 = "  0000000000012345678"
    s11 = "-000000000000001"
    # print(example.myAtoi(s8))
    print(example.myAtoi(s3))#,
          # example.myAtoi(s2),
          # example.myAtoi(s3),
          # example.myAtoi(s4),
          # example.myAtoi(s5),
          # example.myAtoi(s6),
          # example.myAtoi(s7),
          # example.myAtoi(s8),
          # example.myAtoi(s9),
          # example.myAtoi(s10),
          # example.myAtoi(s11))


if __name__ == "__main__":
    main()
