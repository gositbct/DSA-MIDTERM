import heapq

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def find(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            node = node.left if key < node.key else node.right
        return None

    def delete(self, key):
        def _min_node(n):
            while n.left:
                n = n.left
            return n
        def _delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = _min_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            return node
        self.root = _delete(self.root, key)

    def replace(self, old, new):
        if self.find(old):
            self.delete(old)
            self.insert(new)
            return True
        return False

    def inorder(self):
        result = []
        def _in(n):
            if n:
                _in(n.left)
                result.append(n.key)
                _in(n.right)
        _in(self.root)
        return result

    def preorder(self):
        result = []
        def _pre(n):
            if n:
                result.append(n.key)
                _pre(n.left)
                _pre(n.right)
        _pre(self.root)
        return result

    def postorder(self):
        result = []
        def _post(n):
            if n:
                _post(n.left)
                _post(n.right)
                result.append(n.key)
        _post(self.root)
        return result

