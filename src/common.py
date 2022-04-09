# 解题上下文环境依赖


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + ',' + str(self.next)


def new_linklist(*args):
    h = iter = None
    for n in args:
        if not h:
            h = iter = ListNode(n)
        else:
            iter.next = ListNode(n)
            iter = iter.next
    return h