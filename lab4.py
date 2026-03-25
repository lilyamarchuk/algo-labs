RED = True
BLACK = False


class Node:
    def __init__(self, val, prio):
        self.value = val
        self.priority = prio
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None


class RedBlackPriorityQueue:
    def __init__(self):
        self._NIL = Node(None, None)
        self._NIL.color = BLACK
        self._NIL.left = self._NIL
        self._NIL.right = self._NIL
        self._NIL.parent = self._NIL
        self._root = self._NIL

    def insert(self, value, priority):
        z = Node(value, priority)
        z.left = z.right = z.parent = self._NIL
        self._bst_insert(z)
        self._fix_insert(z)

    def extract_max(self):
        if self._root is self._NIL:
            return None
        m = self._leftmost(self._root)
        result = m.value, m.priority
        self._delete_node(m)
        return result

    def peek(self):
        if self._root is self._NIL:
            return None
        m = self._leftmost(self._root)
        return m.value, m.priority

    def _leftmost(self, node):
        while node.left is not self._NIL:
            node = node.left
        return node

    def _bst_insert(self, z):
        p, cur = self._NIL, self._root
        while cur is not self._NIL:
            p = cur
            cur = cur.left if z.priority >= cur.priority else cur.right
        z.parent = p
        if p is self._NIL:
            self._root = z
        elif z.priority >= p.priority:
            p.left = z
        else:
            p.right = z

    def _fix_insert(self, z):
        while z.parent.color == RED:
            if z.parent is z.parent.parent.left:
                u = z.parent.parent.right
                if u.color == RED:
                    z.parent.color = u.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._rotate_left(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rotate_right(z.parent.parent)
            else:
                u = z.parent.parent.left
                if u.color == RED:
                    z.parent.color = u.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._rotate_right(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rotate_left(z.parent.parent)
        self._root.color = BLACK

    def _delete_node(self, z):
        y, y_color = z, z.color
        if z.left is self._NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right is self._NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._leftmost(z.right)
            y_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_color == BLACK:
            self._fix_delete(x)

    def _fix_delete(self, x):
        while x is not self._root and x.color == BLACK:
            if x is x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._rotate_left(x.parent)
                    x = self._root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._rotate_right(x.parent)
                    x = self._root
        x.color = BLACK

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self._NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self._NIL:
            self._root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left, x.parent = x, y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self._NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is self._NIL:
            self._root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right, x.parent = x, y

    def _transplant(self, u, v):
        if u.parent is self._NIL:
            self._root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent