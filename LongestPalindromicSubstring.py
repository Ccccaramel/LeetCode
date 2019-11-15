class Solution:
    def longestPalindrome(self, s: str) -> str:
        s1 = s[::-1]  # 镜像
        left = 0  # 镜像左平移的起始位置
        length = len(s)  # 字符串长度
        maxLength = 0  # 最大长度
        maxStr = ""  # 存储最长字符串
        """
        平移演示
        step1:                                        step2:                               step3:                             step4:                           step5:                         step6:                       step7:                     step8:                   step9:                   step10:                  step11:                     step12:                       step13:                         step14:                           step15:                              step16:                                step14:
        坐标   | 0 1 2 3 4 5 6 7 8                    | 0 1 2 3 4 5 6 7 8                  | 0 1 2 3 4 5 6 7 8                | 0 1 2 3 4 5 6 7 8              | 0 1 2 3 4 5 6 7 8            | 0 1 2 3 4 5 6 7 8          | 0 1 2 3 4 5 6 7 8        | 0 1 2 3 4 5 6 7 8      | 0 1 2 3 4 5 6 7 8      | 0 1 2 3 4 5 6 7 8      | 0 1 2 3 4 5 6 7 8         | 0 1 2 3 4 5 6 7 8           | 0 1 2 3 4 5 6 7 8             | 0 1 2 3 4 5 6 7 8               | 0 1 2 3 4 5 6 7 8                  | 0 1 2 3 4 5 6 7 8                    | 0 1 2 3 4 5 6 7 8
        原始   | c b b c a c a d e                    | c b b c a c a d e                  | c b b c a c a d e                | c b b c a c a d e              | c b b c a c a d e            | c b b c a c a d e          | c b b c a c a d e        | c b b c a c a d e      | c b b c a c a d e      | c b b c a c a d e      | c b b c a c a d e         | c b b c a c a d e           | c b b c a c a d e             | c b b c a c a d e               | c b b c a c a d e                  | c b b c a c a d e                    | c b b c a c a d e
        镜像   |                 e d a c a c b b c    |               e d a c a c b b c    |             e d a c a c b b c    |           e d a c a c b b c    |         e d a c a c b b c    |       e d a c a c b b c    |     e d a c a c b b c    |   e d a c a c b b c    | e d a c a c b b c    e | d a c a c b b c    e d | a c a c b b c       e d a | c a c b b c         e d a c | a c b b c           e d a c a | c b b c             e d a c a c | b b c                e d a c a c b | b c                  e d a c a c b b | c
        判断                     e                                                                         d                                                                 a                                                       a c a                                             c a c                                             c                     c         c                       b                           c b b c【长度 >= 末尾长度 and 长度 > 当前最长,可以 return 了】
        """
        while left <= length:  # 判断镜像左端是否已平移至最右端
            if maxLength >= length-left:
                return maxStr
            left1 = left  # 平移时镜像的左端与遍历时镜像的左端要分开
            left0 = 0  # 原字符串的起始位置,每次遍历都会更改其值,故需要重置
            st = ""  # 存储找到的回文
            print("left1:", left1)
            while left1 < length:  # 开始遍历
                if maxLength >= length-left1:
                    break

                flag = 0  # 标记,等值置 1 ,不等值置 0 ,
                print(s[left0], s1[left1])
                if s[left0] == s1[left1]:  # 找到等值
                    flag += 1
                    st += s[left0]
                    if flag > maxLength and (left1+1 == length or s[left0+1] != s1[left1+1]):
                        maxLength = flag
                        maxStr = st
                else:
                    flag = 0
                    st = ""
                left0 += 1
                left1 += 1

            left += 1
abb
bba

def main():
    s = "abb"  # a cbbd ac babad ccc ababababa
    example = Solution()
    print(example.longestPalindrome(s))


if __name__ == "__main__":
    main()
