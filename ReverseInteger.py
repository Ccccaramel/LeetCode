class Solution:
    def reverse(self, x: int) -> int:
        return (str(abs(x))[::-1])


def main():
    example = Solution()
    num = -123
    print(example.reverse(num))


if __name__ == "__main__":
    main()
