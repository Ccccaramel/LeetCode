# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # while 1:
        #     if l1.val
        pass


def main():
    sol = Solution()
    listNode1 = None
    listNode2 = None

    s = input()  # 输入字符串(合法前提下)
    s = s.replace(" ", "")  # 去除空格
    s = s.replace("(", "")  # 去除括号
    s = s.replace(")", "")  # 去除括号 (2 -> 4 -> 3) + (5 -> 6 -> 4)
    arr = s.split("+")
    for x in range(len(arr)):
        arr[x] = arr[x].split("->")

    node1 = listNode1
    for x in range(len(arr[0])):
        if x == 0:
            listNode1 = ListNode(int(arr[0][x]))
            node1 = listNode1
        else:
            node1.next = ListNode(int(arr[0][x]))
            node1 = node1.next

    node2 = listNode2
    for x in range(len(arr[1])):
        if x == 0:
            listNode2 = ListNode(int(arr[1][x]))
            node2 = listNode2
        else:
            node2.next = ListNode(int(arr[1][x]))
            node2 = node2.next

    print(type(listNode1))
    node = listNode1
    while 1:
        print(node.val,type(node.val))
        node = node.next
        if node is None:
            break

    node = listNode2
    while 1:
        print(node.val,type(node.val))
        node = node.next
        if node is None:
            break
    #
    # print(sol.addTwoNumbers(listNode1, listNode2))


if __name__ == "__main__":
    main()
