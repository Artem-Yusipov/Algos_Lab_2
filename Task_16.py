import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def delete_node(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
        return root
    elif key > root.key:
        root.right = delete_node(root.right, key)
        return root
    if root.left is None and root.right is None:
        return None
    if root.left is None:
        temp = root.right
        root = None
        return temp
    elif root.right is None:
        temp = root.left
        root = None
        return temp
    parent = root
    c_parent = root.right
    while c_parent.left != None:
        parent = c_parent
        c_parent = c_parent.left
    if parent != root:
        parent.left = c_parent.right
    else:
        parent.right = c_parent.right
    root.key = c_parent.key
    return root

def insert_node(node, key):
    if node is None:
        return BSTNode(key)
    if key < node.key:
        node.left = insert_node(node.left, key)
    else:
        node.right = insert_node(node.right, key)
    return node

def fing_k_max_support(root, k, c):
    if root == None or c[0] >= k:
        return
    fing_k_max_support(root.right, k, c)
    c[0] += 1
    if c[0] == k:
        print(root.key)
        return
    fing_k_max_support(root.left, k, c)

def find_k_max(root, k):
    c = [0]
    fing_k_max_support(root, k, c)

n = int(input())
root = None
for i in range(n):
    command = list(input().split())
    match command[0]:
        case '+1':
            root = insert_node(root, int(command[1]))
        case '0':
            find_k_max(root, int(command[1]))
        case '-1':
            root = delete_node(root, int(command[1]))
sys.stdout.close()
