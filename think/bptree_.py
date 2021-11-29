from __future__ import annotations
import sys
from math import floor

class Node:
    uid_counter = 0
    def __init__(self, order):
        self.order = order
        self.parent: Node = None
        self.keys = []
        self.values = []

        #node id
        Node.uid_counter+=1
        self.uid = self.uid_counter

    def split(self) -> Node:
        left = Node(self.order)
        right = Node(self.order)
        #우측 첫번째 요소 키설정을 위한 변수
        mid = int(self.order // 2)

        #부모 설정
        left.parent = right.parent = self

        left.keys = self.keys[:mid]
        left.values = self.values[:mid + 1]
        right.keys = self.keys[mid + 1:]
        right.values = self.values[mid + 1:]

        #
        self.values = [left, right]
        self.keys = [self.keys[mid]]

        for child in left.values:
            if isinstance(child, Node):
                child.parent = left
        for child in right.values:
            if isinstance(child, Node):
                child.parent = right

        return self

    def get_size(self) -> int:
        return len(self.keys)

    def is_empty(self) -> bool:
        return len(self.keys) == 0

    def is_full(self) -> bool:
        return len(self.keys) == self.order - 1

    def is_nearly_underflowed(self) -> bool:
        return len(self.keys) <= floor(self.order / 2)

    def is_underflowed(self) -> bool:
        return len(self.keys) <= floor(self.order / 2) - 1

    def is_root(self) -> bool:
        return self.parent is None


class LeafNode(Node):
    def __init__(self, order):
        super().__init__(order)
        self.prev_leaf: LeafNode = None
        self.next_leaf: LeafNode = None

    def add(self, key, value):
        if not self.keys:
            self.keys.append(key)
            self.values.append([value])
            return

        for i, item in enumerate(self.keys):
            if key == item:
                self.values[i].append(value)
                break

            elif key < item:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                self.values = self.values[:i] + [[value]] + self.values[i:]
                break

            elif i + 1 == len(self.keys):
                self.keys.append(key)
                self.values.append([value])
                break

    def split(self) -> Node:
        top = Node(self.order)
        right = LeafNode(self.order)
        mid = int(self.order // 2)

        self.parent = right.parent = top

        right.keys = self.keys[mid:]
        right.values = self.values[mid:]
        right.prev_leaf = self
        right.next_leaf = self.next_leaf

        top.keys = [right.keys[0]]
        top.values = [self, right]

        self.keys = self.keys[:mid]
        self.values = self.values[:mid]
        self.next_leaf = right

        return top


class B_PLUS_TREE(object):
    def __init__(self, order):
        #order 설정
        #처음엔 leafNode가 됨
        self.order: int = order
        self.root: Node = LeafNode(order)

    @staticmethod
    def _find(node: Node, key):
        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i
            elif i + 1 == len(node.keys):
                return node.values[i + 1], i + 1

    def find(self, key):
        if key not in B_PLUS_TREE.all_data(self):
            print('NONE')
            return
        node = self.root
        print(node.keys, end='-')
        while not isinstance(node, LeafNode):
            node, index = self._find(node, key)
            print(node.keys, end='-')

        for i, item in enumerate(node.keys):
            if key == item:
                return node.values[i]
        print()
        return None

    def all_data(self):
        node = self.get_leftmost_leaf()
        list_ = []
        if not node:
            return None

        while node:
            for node_data in node.values:
                list_.append(node_data[0])

            node = node.next_leaf

        return list_

    def _merge_up(parent: Node, child: Node, index):
        parent.values.pop(index)
        pivot = child.keys[0]

        for c in child.values:
            if isinstance(c, Node):
                c.parent = parent

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + child.values + parent.values[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += child.values
                break

    def insert(self, key):
        value = key
        node = self.root

        while not isinstance(node, LeafNode):
            node, index = self._find(node, key)

        node.add(key, value)

        while len(node.keys) == node.order:
            if not node.is_root():
                parent = node.parent
                node = node.split()
                jnk, index = self._find(parent, node.keys[0])
                self._merge_up(parent, node, index)
                node = parent
            else:
                node = node.split()
                self.root = node


    def delete(self, key):
        node = self.root

        while not isinstance(node, LeafNode):
            node, parent_index = self._find(node, key)

        if key not in node.keys:
            return False

        index = node.keys.index(key)
        node.values[index].pop()  # Remove the last inserted data.

        if len(node.values[index]) == 0:
            node.values.pop(index)  # Remove the list element.
            node.keys.pop(index)

            while node.is_underflowed() and not node.is_root():
                # Borrow attempt:
                prev_sibling = B_PLUS_TREE.get_prev_sibling(node)
                next_sibling = B_PLUS_TREE.get_next_sibling(node)
                jnk, parent_index = self._find(node.parent, key)

                if prev_sibling and not prev_sibling.is_nearly_underflowed():
                    self._borrow_left(node, prev_sibling, parent_index)
                elif next_sibling and not next_sibling.is_nearly_underflowed():
                    self._borrow_right(node, next_sibling, parent_index)
                elif prev_sibling and prev_sibling.is_nearly_underflowed():
                    self._merge_on_delete(prev_sibling, node)
                elif next_sibling and next_sibling.is_nearly_underflowed():
                    self._merge_on_delete(node, next_sibling)

                node = node.parent

            if node.is_root() and not isinstance(node, LeafNode) and len(node.values) == 1:
                self.root = node.values[0]
                self.root.parent = None

    @staticmethod
    def _borrow_left(node: Node, sibling: Node, parent_index):
        if isinstance(node, LeafNode):
            key = sibling.keys.pop(-1)
            data = sibling.values.pop(-1)
            node.keys.insert(0, key)
            node.values.insert(0, data)

            node.parent.keys[parent_index - 1] = key
        else:
            parent_key = node.parent.keys.pop(-1)
            sibling_key = sibling.keys.pop(-1)
            data: Node = sibling.values.pop(-1)
            data.parent = node

            node.parent.keys.insert(0, sibling_key)
            node.keys.insert(0, parent_key)
            node.values.insert(0, data)

    @staticmethod
    def _borrow_right(node: LeafNode, sibling: LeafNode, parent_index):
        if isinstance(node, LeafNode):
            key = sibling.keys.pop(0)
            data = sibling.values.pop(0)
            node.keys.append(key)
            node.values.append(data)
            node.parent.keys[parent_index] = sibling.keys[0]
        else:
            parent_key = node.parent.keys.pop(0)
            sibling_key = sibling.keys.pop(0)
            data: Node = sibling.values.pop(0)
            data.parent = node

            node.parent.keys.append(sibling_key)
            node.keys.append(parent_key)
            node.values.append(data)

    @staticmethod
    def _merge_on_delete(l_node: Node, r_node: Node):
        parent = l_node.parent

        jnk, index = B_PLUS_TREE._find(parent, l_node.keys[0])
        parent_key = parent.keys.pop(index)
        parent.values.pop(index)
        parent.values[index] = l_node

        if isinstance(l_node, LeafNode) and isinstance(r_node, LeafNode):
            l_node.next_leaf = r_node.next_leaf
        else:
            l_node.keys.append(parent_key)  # TODO Verify dis
            for r_node_child in r_node.values:
                r_node_child.parent = l_node

        l_node.keys += r_node.keys
        l_node.values += r_node.values

    @staticmethod
    def get_prev_sibling(node: Node) -> Node:
        if node.is_root() or not node.keys:
            return None
        jnk, index = B_PLUS_TREE._find(node.parent, node.keys[0])
        return node.parent.values[index - 1] if index - 1 >= 0 else None

    @staticmethod
    def get_next_sibling(node: Node) -> Node:
        if node.is_root() or not node.keys:
            return None
        jnk, index = B_PLUS_TREE._find(node.parent, node.keys[0])

        return node.parent.values[index + 1] if index + 1 < len(node.parent.values) else None

    def get_leftmost_leaf(self):
        if not self.root:
            return None

        node = self.root
        while not isinstance(node, LeafNode):
            node = node.values[0]

        return node

    def get_rightmost_leaf(self):
        if not self.root:
            return None

        node = self.root
        while not isinstance(node, LeafNode):
            node = node.values[-1]

    @staticmethod
    def intersperse(lst, item):
        result = [item] * (len(lst) * 2)
        result[0::2] = lst
        return result

    def print_root(self):
        l = "["
        for k in self.root.keys:
            l += "{},".format(k)
        l = l[:-1] + "]"
        print(l)
        pass
    
    def print_tree(self):
        if self.root.is_empty():
            print('The B+ Tree is empty!')
            return
        queue = [self.root, 0]
        temp_parent = self.root
        print(self.root.keys, end='-')

        while len(queue) > 0:
            node = queue.pop(0)
            height = queue.pop(0)

            if not isinstance(node, LeafNode):
                queue += self.intersperse(node.values, height + 1)
            if height == 0:
                continue

            if temp_parent.uid != node.parent.uid:
                temp_parent = node.parent
                print()
                print(node.parent.keys, end='-')
                print(node.keys, end=',')
            else:
                print(node.keys, end=',')

    def find_range(self, k_from, k_to):
        node = self.get_leftmost_leaf()
        if not node:
            return None
        while node:
            for node_data in node.values:
                if node_data[0] >= k_from and node_data[0] <= k_to:
                    print('{}'.format(', '.join(map(str, node_data))), end=',')

            node = node.next_leaf


def main():
    myTree = None
    
    while (True):
        comm = sys.stdin.readline()
        comm = comm.replace("\n", "")
        params = comm.split()
        if len(params) < 1:
            continue
        
        print(comm)
        
        if params[0] == "INIT":
            order = int(params[1])
            myTree = B_PLUS_TREE(order)
            
        elif params[0] == "EXIT":
            return
            
        elif params[0] == "INSERT":
            k = int(params[1])
            myTree.insert(k)
            
        elif params[0] == "DELETE":
            k = int(params[1])
            myTree.delete(k)            
            
        elif params[0] == "ROOT":            
            myTree.print_root()            
            
        elif params[0] == "PRINT":            
            myTree.print_tree()            
                  
        elif params[0] == "FIND":            
            k = int(params[1])
            myTree.find(k)
            
        elif params[0] == "RANGE":            
            k_from = int(params[1])
            k_to = int(params[2])
            myTree.find_range(k_from, k_to)
        
        elif params[0] == "SEP":
            print("-------------------------")
    
if __name__ == "__main__":
    main()