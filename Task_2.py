import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')


class BST:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.key

    def is_exists(self, key):
        if key == self.key:
            return True
        if key < self.key:
            if self.left is None:
                return False
            return self.left.is_exists(key)
        if self.right is None:
            return False
        return self.right.is_exists(key)

    def insert_node(self, key):
        if not self.key:
            self.key = key
            return
        if self.key == key:
            return
        if key < self.key:
            if self.left:
                self.left.insert_node(key)
                return
            self.left = BST(key)
            return
        if self.right:
            self.right.insert_node(key)
            return

        self.right = BST(key)


def main():
    bst = BST()
    while True:
        try:
            command, num = map(str, input().split())
            num = int(num)
            if command == '+':
                bst.insert_node(num)
            else:
                maximum = bst.get_max()
                flag = False
                for i in range(num+1, maximum+1):
                    if bst.is_exists(i):
                        print(i)
                        flag = True
                        break
                if not flag:
                    print(0)
        except:
            break
main()
