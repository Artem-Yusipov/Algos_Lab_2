import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')


class Tree_node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def is_BTS(root, l=None, r=None):
    if root == None:
        return True
    if l != None and root.data <= l.data:
        return False
    if r != None and root.data >= r.data:
        return False
    return is_BTS(root.left, l, root) and is_BTS(root.right, root, r)


def main():
    n = int(input())
    if n == 0:
        print("YES")
    else:
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

        if is_BTS(tree_list[0]):
            print("YES")
        else:
            print("NO")
    sys.stdout.close()

main()

