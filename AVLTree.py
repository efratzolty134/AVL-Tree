# username - efratzolty
# id1      - 206361164
# name1    - Efrat Zolty
# id2      - 318900024
# name2    - Shir Ripstein


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @type value: any
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        return self.parent

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        return self.height

    """ added function that returns the Balance Factor

    @rtype: int
    @returns: the Balance Factor of self
    """

    def get_bf(self):
        return self.left.get_height() - self.right.get_height()

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        if self.key is None:
            return False
        return True


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None
        self.tree_size = 0

    # add your fields here

    """searches for a AVLNode in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: the AVLNode corresponding to key or None if key is not found.
    """

    def search(self, key):
        curr = self.get_root()
        while (curr is not None) and curr.is_real_node():
            if curr.get_key() == key:
                return curr
            elif curr.get_key() > key:
                curr = curr.get_left()
            else:
                curr = curr.get_right()
        return None

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key, val):
        rebalance_num = 0
        node = AVLNode(key, val)
        left = AVLNode(None, None)  # virtual left son
        right = AVLNode(None, None)  # virtual right son
        node.set_left(left)
        left.set_parent(node)
        node.set_right(right)
        right.set_parent(node)
        node.set_height(0)
        curr = self.get_root()

        if curr is None:  # if the tree is empty
            self.root = node
            self.tree_size += 1
            return rebalance_num

        while curr.is_real_node():
            if curr.get_key() > key:
                if curr.get_left().is_real_node():
                    curr = curr.get_left()
                else:  # put the node as left son
                    curr.set_left(node)
                    node.set_parent(curr)
                    break

            elif curr.get_key() < key:
                if curr.get_right().is_real_node():
                    curr = curr.get_right()
                else:  # put the node as right son
                    curr.set_right(node)
                    node.set_parent(curr)
                    break

        self.tree_size += 1
        y = node.get_parent()
        """correction after insertion using fix_AVL method"""
        return self.fix_AVL(y)

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):
        rebalance_num = 0
        v = node
        """if the node that needs to be deleted has two real sons we switch between the node and his successor"""
        if v.get_left().is_real_node() and v.get_right().is_real_node():
            temp = v
            temp_height = temp.get_height()
            v = self.get_successor(v)
            v_height = v.get_height()
            parent_temp = temp.get_parent()
            temp_right = temp.get_right()
            temp_left = temp.get_left()
            v_parent = v.get_parent()
            v_right = v.get_right()
            v_left = v.get_left()  # will be a virtual node anyway
            v.set_height(temp_height)
            temp.set_height(v_height)

            """if the deleted node is not the root we will set v as the child of node's parent"""
            if not temp.get_key() == self.get_root().get_key():
                if self.is_left_son(parent_temp, temp):
                    parent_temp.set_left(v)
                else:
                    parent_temp.set_right(v)

            else:
                self.root = v

            """if the successor is the right child of the node"""
            if temp_right.get_key() == v.get_key():
                temp.set_parent(v)
                v.set_right(temp)
            else:
                temp.set_parent(v_parent)
                v_parent.set_left(temp)
                v.set_right(temp_right)
                temp_right.set_parent(v)

            """changes in the connections of the two nodes"""
            temp_left.set_parent(v)
            v.set_left(temp_left)
            v.set_parent(parent_temp)
            v_right.set_parent(temp)
            v_left.set_parent(temp)
            temp.set_right(v_right)
            temp.set_left(v_left)
            v = temp

        y = v.get_parent()
        """now it is guarenteed that the deleted node has only one child"""
        if v.get_left().is_real_node():
            son = v.get_left()
        else:
            son = v.get_right()

        """if the deleted node is the root"""
        if v.get_key() == self.get_root().get_key():
            if son.is_real_node():
                self.root = son
                son.set_parent(None)
            else:  # if the root is the only node
                self.root = None

        else:
            if self.is_left_son(y, v):
                y.set_left(son)
            else:
                y.set_right(son)
            son.set_parent(y)

        self.tree_size -= 1

        """correction after deletion using fix_AVL method"""
        return self.fix_AVL(y)

    """performs the needed changes in the tree in order to maintain it as an AVL tree"""

    def fix_AVL(self, node):
        rebalance_num = 0
        while node is not None:
            change = False
            max_height = max(node.get_right().get_height(),
                             node.get_left().get_height())  # max between the sons' heights
            old_height = node.get_height()

            if old_height != max_height + 1:
                node.set_height(max_height + 1)
                change = True

            bf = node.get_bf()
            if -2 < bf < 2:  # node has a legal balance factor
                if not change:  # node's height hasn't changed, no need to continue
                    return rebalance_num
                else:  # node's height has changed, continue fixing the tree with node's parent
                    rebalance_num += 1
                    node = node.get_parent()

            elif bf == 2 or bf == -2:  # node is a criminal node, perform rotation and finish
                parent = node.get_parent()
                rebalance_num += self.rotation(node)
                node = parent
        return rebalance_num

    """returns True if the node is left son of parent, and False otherwise"""

    def is_left_son(self, parent, node):
        if parent.get_left().get_key() == node.get_key():
            return True
        return False

    def left_rotation(self, node):
        son = node.get_right()
        grand_father = node.get_parent()
        l = son.get_left()
        node.set_right(l)
        l.set_parent(node)
        son.set_parent(grand_father)
        if grand_father is not None:
            if self.is_left_son(grand_father, node):
                grand_father.set_left(son)
            else:
                grand_father.set_right(son)
        else:
            self.root = son

        son.set_left(node)
        node.set_parent(son)
        node.set_height(1 + max(node.get_left().get_height(), node.get_right().get_height()))
        son.set_height(1 + max(son.get_left().get_height(), son.get_right().get_height()))

    def right_rotation(self, node):
        son = node.get_left()
        grand_father = node.get_parent()
        r = son.get_right()
        node.set_left(r)
        r.set_parent(node)
        son.set_parent(grand_father)
        if grand_father is not None:
            if self.is_left_son(grand_father, node):
                grand_father.set_left(son)
            else:
                grand_father.set_right(son)
        else:
            self.root = son

        son.set_right(node)
        node.set_parent(son)
        node.set_height(1 + max(node.get_left().get_height(), node.get_right().get_height()))
        son.set_height(1 + max(son.get_left().get_height(), son.get_right().get_height()))

    """the function performs the needed rotation and returns the number of rebalancing operations"""

    def rotation(self, node):
        bf = node.get_bf()
        if bf == -2:
            son = node.get_right()
            """left rotation"""
            if son.get_bf() == -1 or son.get_bf() == 0:
                self.left_rotation(node)
                return 1
            """right then left rotation"""
            if son.get_bf() == 1:
                self.right_rotation(son)
                self.left_rotation(node)
                return 2
        elif bf == 2:
            son = node.get_left()
            """right rotation"""
            if son.get_bf() == 1 or son.get_bf() == 0:
                self.right_rotation(node)
                return 1
            """left then right rotation"""
            if son.get_bf() == -1:
                self.left_rotation(son)
                self.right_rotation(node)
                return 2
        return 0

    """returns the successor of the node in assuming he has a right child"""

    def get_successor(self, node):
        succ = node.get_right()
        while (succ is not None) and succ.get_left().is_real_node():
            succ = succ.get_left()
        return succ

    """returns an array representing dictionary 
    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure"""

    def avl_to_array(self):
        arr = []
        s = []
        curr = self.get_root()
        if curr is None:
            return arr
        while (curr.is_real_node() or len(s) != 0):
            while curr.is_real_node():
                s.append(curr)
                curr = curr.get_left()
            curr = s.pop()
            arr.append((curr.get_key(), curr.get_value()))
            curr = curr.get_right()
        return arr

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary """

    def size(self):
        return self.tree_size

    """splits the dictionary at the i'th index

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key."""

    def split(self, node):
        t1 = AVLTree()  # set base tree for the left tree
        if node.get_left().is_real_node():
            t1.root = node.get_left()
            t1.get_root().set_parent(None)

        t2 = AVLTree()  # set base tree for the right tree
        if node.get_right().is_real_node():
            t2.root = node.get_right()
            t2.get_root().set_parent(None)

        parent = node.get_parent()
        node.set_parent(None)
        temp = AVLTree()

        """iterate over the nodes in the path from the node we split the tree by,to the root"""
        while parent is not None:
            """if the node is the right son of his father"""
            if not self.is_left_son(parent, node):
                """extract parent's left subtree and join it with the left base tree using parent as the connecting node"""
                temp.root = parent.get_left()
                parent.set_right(AVLNode(None, None))
                parent.set_left(AVLNode(None, None))
                temp.get_root().set_parent(None)
                t1.join(temp, parent.get_key(), parent.get_value())

            else:
                """extract parent's right subtree and join it with the right base tree using parent as the connecting node"""
                temp.root = parent.get_right()
                parent.set_left(AVLNode(None, None))
                parent.set_right(AVLNode(None, None))
                temp.get_root().set_parent(None)
                t2.join(temp, parent.get_key(), parent.get_value())

            node = parent
            parent = parent.get_parent()
            node.set_parent(None)

        """deactivate the node we splitted the tree by"""
        node.set_key(None)
        node.set_value(None)
        node.set_left(None)
        node.set_right(None)
        node.set_parent(None)
        node.set_height(-1)

        return [t1, t2]

    """joins self with key and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree2
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree2, key, val):
        x = AVLNode(key, val)

        if self.get_root() is None or self.get_root().get_key() is None:  # if self is empty
            # if both trees are empty we will set x as the root of the joined tree and return it
            if tree2.get_root() is None or tree2.get_root().get_key() is None:
                self.insert(key,val)
                self.root = x
                self.tree_size = 1
                return 1

            else:  # if self is empty but tree2 isn't empty we will insert x to tree2 and set self as tree
                tree2.insert(key, val)
                self.root = tree2.get_root()
                self.tree_size = tree2.tree_size
                tree2.root = None
                tree2.tree_size = 0
                return self.get_root().get_height() + 1

        elif tree2.get_root() is None or tree2.get_root().get_key() is None:  # if self isn't empty but tree2 is empty
            self.insert(key, val)
            return self.get_root().get_height() + 1

        else:  # if both self and tree =2 aren't empty
            if self.get_root().get_key() < tree2.get_root().get_key():
                t1 = self
                t2 = tree2
            else:
                t1 = tree2
                t2 = self

        root1 = t1.get_root()
        root2 = t2.get_root()

        height1 = root1.get_height()
        height2 = root2.get_height()

        if height1 < height2:
            curr = root2
            while curr.get_height() > height1:
                curr = curr.get_left()

            old_parent = curr.get_parent()

            x.set_left(root1)
            root1.set_parent(x)

            x.set_right(curr)
            curr.set_parent(x)
            x.set_parent(old_parent)
            x.set_height(1 + max(x.get_left().get_height(), x.get_right().get_height()))

            if old_parent is not None:
                old_parent.set_left(x)
            else:
                t2.root = x

            y = old_parent
            while y is not None:
                if y.get_bf() == 2:
                    self.right_rotation(y)
                else:
                    y.set_height(1 + max(y.get_left().get_height(), y.get_right().get_height()))
                y = y.get_parent()

            self.root = t2.get_root()

        else:
            curr = root1
            while curr.get_height() > height2:
                curr = curr.get_right()

            old_parent = curr.get_parent()

            x.set_left(curr)
            curr.set_parent(x)

            x.set_right(root2)
            root2.set_parent(x)
            x.set_parent(old_parent)
            x.set_height(1 + max(x.get_left().get_height(), x.get_right().get_height()))

            if old_parent is not None:
                old_parent.set_right(x)
            else:
                t1.root = x

            y = old_parent
            while y is not None:
                if y.get_bf() == -2:
                    self.left_rotation(y)
                else:
                    y.set_height(1 + max(y.get_left().get_height(), y.get_right().get_height()))
                y = y.get_parent()

            self.root = t1.get_root()

        self.tree_size += tree2.tree_size + 1
        tree2.root = None
        tree2.tree_size = 0

        return abs(height1 - height2) + 1

    """returns the root of the tree representing the dictionary
    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty"""

    def get_root(self):
        return self.root