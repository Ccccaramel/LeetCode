class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        maxV = 0
        space = 0
        for i in range(len(s)):
            if s[i] in dic and space <= dic[s[i]]:
                space = dic[s[i]]+1
            else:
                maxV = max(maxV, i-space+1)
            dic[s[i]] = i
        return maxV


def main():
    example = Solution()
    s = "abcabcbb"
    print(example.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()
