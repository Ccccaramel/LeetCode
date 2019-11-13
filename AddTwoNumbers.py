# Definition for singly-linked list.



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = None
        listNode3 = l3
        mark = 0
        while 1:
            if l1 is None and l2 is None:
                if mark == 1:
                    listNode3.next = ListNode(1)
                return l3
            if l1 is None:
                add = l2.val
            elif l2 is None:
                add = l1.val
            else:
                add = l1.val+l2.val

            if mark == 1:  # 判断前一位是否有进位  (5)+(5)
                add += 1  # 有进位,和加 1
                mark = 0  # 进位标记置 0

            if add > 9:  # 判断本位是否有进位
                mark = 1  # 设置进位标记为 1
                add -= 10  # 更改为 1 位数

            if l1 is not None or l2 is not None or mark == 0:
                if l3 is None:
                    l3 = ListNode(add)
                    listNode3 = l3
                else:
                    listNode3.next = ListNode(add)
                    listNode3 = listNode3.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

def main():
    sol = Solution()
    listNode1 = None
    listNode2 = None

    s = input()  # 输入字符串(合法前提下)
    s = s.replace(" ", "")  # 去除空格
    s = s.replace("(", "")  # 去除括号 (1->8)+(0)
    s = s.replace(")", "")  # 去除括号 (2 -> 4 -> 3) + (5 -> 6 -> 4)
    arr = s.split("+")
    for x in range(len(arr)):
        arr[x] = arr[x].split("->")

    print(arr)
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

    # print(type(listNode1))
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
    lis = sol.addTwoNumbers(listNode1, listNode2)
    while 1:
        if lis is not None:
            print("->",lis.val)
            lis = lis.next


if __name__ == "__main__":
    main()
