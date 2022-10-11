import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')


class Tree_node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Height:
    def __init__(self):
        self.height = 0


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def is_balanced(root):
    if root is None:
        return True

    lh = Height()
    rh = Height()
    lh.height = height(root.left)
    rh.height = height(root.right)
    print(rh.height - lh.height)
    l = is_balanced(root.left)
    r = is_balanced(root.right)
    if abs(lh.height - rh.height) <= 1:
        return l and r
    return False


n = int(input())
if n != 0:
    tree_list = [Tree_node(0) for i in range(n)]
    for i in range(n):
        val, left, right = map(int, input().split())
        left -= 1
        right -= 1
        tree_list[i].data = val
        if left != -1:
            tree_list[i].left = tree_list[left]
        if right != -1:
            tree_list[i].right = tree_list[right]

is_balanced(tree_list[0])

