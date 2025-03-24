AVL-Tree
This repository contains a Python implementation of an AVL Tree, a self-balancing binary search tree that maintains logarithmic height through rotations. This ensures efficient insertion, deletion, and search operations.

AVLNode Class

  The `AVLNode` class represents a node in the AVL Tree. It supports both real and virtual nodes. Virtual nodes simplify the 
  tree operations and are defined with no key, no value, and height -1.
   
  Methods:
  - `get_key()`  
    Returns the key of the node (an integer), or `None` if the node is virtual.
    
  - `get_value()`  
    Returns the value (`info`) stored in the node, or `None` if the node is virtual.
  
  - `get_left()`  
    Returns the left child node (another `AVLNode`), or `None` if not set.
  
  - `get_right()`  
    Returns the right child node, or `None` if not set.
  
  - `get_parent()`  
    Returns the parent node, or `None` if this node is the root or unlinked.
  
  - `is_real_node()`  
    Returns `True` if this is a real node (i.e., not virtual), otherwise `False`.
  
  - `get_height()`  
    Returns the height of the node. Virtual nodes return `-1` by definition.
  
  - `set_left(node)`  
    Sets the given node as the left child of the current node.
  
  - `set_right(node)`  
    Sets the given node as the right child of the current node.
  
  - `set_parent(node)`  
    Sets the given node as the parent of the current node.
  
  - `set_key(key)`  
    Sets the key of the current node.
  
  - `set_value(value)`  
    Sets the value (`info`) of the current node.
  
  - `set_height(height)`  
    Sets the height of the current node.
  
  - `get_balance_factor()`  
    Calculates and returns the balance factor of the node:  
    `height(left) - height(right)`
  
  - `update_height()`  
    Recalculates the height of the current node based on its children's heights.
    
AVLTree Class

  The `AVLTree` class implements an AVL self-balancing binary search tree.

  Methods:
  - `insert(key, value)`
    Inserts a new node with the given key and value. Assumes the key is not already in the tree.
    Returns the number of rotations (balance operations) performed.

  - `delete(node)`  
    Deletes the given node from the tree and returns the number of rotations (balance operations) needed to maintain the AVL
    property.
  
  - `search(key)`  
    Returns the node containing the given key, or `None` if not found.
  
  - `get_root()`  
    Returns the root node of the AVL tree.
  
  - `avl_to_array()`  
    Returns a sorted list of `(key, value)` pairs from an in-order traversal of the tree.
  
  - `size()`  
    Returns the total number of real (non-virtual) nodes in the tree.
  
  - `split(node)`  
    Splits the tree into two AVL trees at the given node. The node itself is removed in the process.  
    Returns a tuple of two AVL trees:  
    `(tree_with_keys_smaller_than_x, tree_with_keys_greater_than_x)`
  
  - `join(other_tree, key, value)`
    Joins the current tree with another AVL tree and a node `(key, value)` between them.  
    Assumes all keys in `other_tree` are either all smaller or all greater.  
    Returns the number of balancing operations (rotations) performed.
  
  
    
