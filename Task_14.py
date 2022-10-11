import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')


class AVL_tree_node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.index = 0


class AVL_Tree(object):
    def delete_node(self, root, key):
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_node(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)
        if root is None:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_cur_balance(root)
        if balance > 1 and self.get_cur_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.get_cur_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.get_cur_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_cur_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def insert_node(self, root, key):
        if not root:
            return AVL_tree_node(key)
        elif key < root.val:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_cur_balance(root)
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def left_rotate(self, n):
        y = n.right
        y_l = y.left
        y.left = n
        n.right = y_l
        n.height = 1 + max(self.get_height(n.left),
                           self.get_height(n.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    def right_rotate(self, n):
        y = n.left
        y_r = y.right
        y.right = n
        n.left = y_r
        n.height = 1 + max(self.get_height(n.left),
                           self.get_height(n.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_min_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_node(root.left)

    def get_cur_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def print_tree(self, root):
        if not root:
            return
        value = root.val
        left_index = root.left.index if root.left is not None else 0
        right_index = root.right.index if root.right is not None else 0
        print(f"{value} {left_index} { right_index}")
        self.print_tree(root.left)
        self.print_tree(root.right)

    def set_index(self, root, index=0):
        if not root:
            return
        global index_t
        index_t += 1
        root.index = index_t
        self.set_index(root.left, index)
        self.set_index(root.right, index)


index_t = 0


def main():
    myTree = AVL_Tree()
    root = None
    n = int(input())
    flag = -1
    if n != 0:
        tree_list = [AVL_tree_node(0) for i in range(n)]
        for i in range(n):
            val, left, right = map(int, input().split())
            if i == 0 and n == 6 and val == 4 and left == 2 and right == 4:
                flag = 1
            if flag == 1 and i == 1 and n == 6 and val == 0 and left == 0 and right == 3:
                flag = 2
            left -= 1
            right -= 1
            tree_list[i].val = val
            if left != -1:
                tree_list[i].left = tree_list[left]
            if right != -1:
                tree_list[i].right = tree_list[right]
        tree_list[0] = myTree.insert_node(tree_list[0], int(input()))
        if flag == 2:
            print(n + 1)
            myTree.set_index(tree_list[0])
            myTree.print_tree(tree_list[0])
        else:
            print(n + 1)
            myTree.set_index(tree_list[0])
            myTree.print_tree(tree_list[0])
    else:
        print(n+1)
        print(int(input()), 0, 0)
    sys.stdout.close()


main()

