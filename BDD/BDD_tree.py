# body of node in tree
class Node:
    def __init__(self, function):
        self.left_child = None
        self.right_child = None
        self.function = function
        self.parent = None
        self.variable_count=None


# BDD tree
class BDD:
    # constructor with root of the tree,order of boolean arguments, num of unique nodes, num of variable count
    # and a dictiory that stores all used nodes
    def __init__(self):
        self.root = None
        self.order = None
        self.used_nodes = {}
        self.unique_nodes = 0
        self.variable_count = 0

    # fucntion which creates the root and starts the creation of the tree
    def create(self, function, order):
        self.root = Node(function)
        self.order = order
        self._create(self.root.function, self.root, self.order)
        self.reduce(self.root)
        self.unique_nodes = len(self.used_nodes)
        self.variable_count = self.root.variable_count
        return self.root

    # function which creates additional nodes for the tree and calls itself recursivly
    def _create(self, function, current_node: Node, order: list):

        # when we encounter node with value of 1 or 0 end the recursion branch
        if order == [] or isinstance(function, int):
            return
        current_function = function.split("+")  # split current function into a list
        left_child = self._create_left_child(current_function,
                                             order)  # list to store arguments for left child of the current node
        right_child = self._create_right_child(current_function,
                                               order)  # list to store arguments for the right child of the current node

        # if _create_left_child return 1, create a node with value 1
        if left_child == 1:
            current_node.left_child = self.reduce(Node(1))
        # if left_child list is not empty create node with remaining function
        elif left_child != []:
            current_node.left_child = (self.reduce(Node("+".join(left_child))))  # creation of new node with reduction
        # if left child list is empty meaning we reached the end of the branch create 1 or 0 node
        else:
            index = current_function[0].find(order[0])
            if "!" + order[0] in current_function[0]:
                current_node.left_child = (
                    self.reduce(Node(1)))  # creation of new node with reduction
            if order[0] in current_function[0] and current_function[0][index - 1] != "!":
                current_node.left_child = (
                    self.reduce(Node(0)))  # creation of new node with reduction

        # if _create_left_child return 1, create a right child node with value 1
        if right_child == 1:
            current_node.right_child = self.reduce(Node(1))
        # if right_child list is not empty create node with remaining function
        elif right_child != []:
            # creation of new node with reduction
            current_node.right_child = (self.reduce(Node("+".join(right_child))))
        # if right child list is empty meaning we reached the end of the branch create 1 or 0 node
        else:
            index = current_function[0].find(order[0])
            if "!" + order[0] in current_function[0]:
                current_node.right_child = (
                    self.reduce(Node(0)))  # creation of new node with reduction
            if order[0] in current_function[0] and current_function[0][index - 1] != "!":
                current_node.right_child = (
                    self.reduce(Node(1)))  # creation of new node with reduction

        # when we get situation where X +!X is the current function we need to create left and right child with value 1
        # i needed to hard code this in because my previous code would count for this situation
        if self._zero_and_one(function) == 1:
            current_node.left_child = (self.reduce(Node(1)))  # creation of new node with reduction
            current_node.right_child = (self.reduce(Node(1)))  # creation of new node with reduction

        # setting current_node variable count for correct functioning of the use function in BDD tree
        current_node.variable_count = len(order)

        # setting current node as parent for newly created nodes
        current_node.left_child.parent = current_node
        current_node.right_child.parent = current_node

        # checking if node is redundant
        try:
            if self.check_redundant(current_node) == True:

                if current_node == current_node.parent.left_child:
                    current_node.parent.left_child = current_node.left_child
                    current_node = current_node.left_child
                    self._create(current_node.function, current_node,
                                 order[1:])  # recursion to create children for reduced node

                else:
                    current_node.parent.right_child = current_node.right_child
                    current_node = current_node.right_child
                    self._create(current_node.function, current_node,
                                 order[1:])  # recursion to create children for reduced node

            # if node is not redundant continue traversing tree
            else:
                # calling this function recursivly to traverse the tree
                self._create(current_node.left_child.function, current_node.left_child, order[1:])
                self._create(current_node.right_child.function, current_node.right_child, order[1:])
        except:
            ...
    # function which returns list of arguments for left_child
    def _create_left_child(self, current_function, order: list):
        left_child = []
        for i in range(len(current_function)):
            if current_function[i] == "!" + order[0]:
                return 1  # returns 1 if we need to create a Node with value 1
            index = current_function[i].find(order[0])  # get index of current order to dissassamble current function

            if ("!" + order[0]) in current_function[i]:
                if self._removeChar(current_function[i], "!" + order[0]) != "":
                    # if !X(current order element) is in current KNF, append to left_child list
                    left_child.append(self._removeChar(current_function[i], "!" + order[0]))
            elif order[0] not in current_function[i] and "!" + order[0] not in current_function[i]:
                # if X or !X (current order element) is not in current KNF
                left_child.append(current_function[i])
        return left_child

    # function which returns list of arguments for right_child
    def _create_right_child(self, current_function, order: list):
        right_child = []
        for i in range(len(current_function)):
            if current_function[i] == order[0]:
                return 1  # returns 1 if we need to create a Node with value 1
            index = current_function[i].find(order[0])  # get index of current order to dissassamble current function
            if order[0] in current_function[i] and current_function[i][index - 1] != "!":
                if self._removeChar(current_function[i], order[0]) != "":
                    # if X(current order elements) is in current KNF , append to right_child list
                    right_child.append(self._removeChar(current_function[i], order[0]))
            elif order[0] not in current_function[i] and "!" + order[0] not in current_function[i]:
                # if X or !X (current order element) is not in current KNF
                right_child.append(current_function[i])
        return right_child

    # helper function which removes char from string
    def _removeChar(self, function, remove_char):
        return function.replace(remove_char, "")

    # helper function which return length
    def _return_variable_count(self, function):
        if function is int:
            return 0
        current_function = function
        unique_variables = []
        current_function = current_function.replace("!", "")
        current_function = current_function.replace("+", "")
        for i in range(len(current_function)):
            if current_function[i] not in unique_variables:
                unique_variables.append(current_function[i])
        return len(unique_variables)

    # helper function which checks if function = X+!X
    def _zero_and_one(self, function):
        if len(function) == 4:
            if function.count(function[-1]) == 2 and "!" in function:
                return 1
        else:
            return 0

    # function which starts the use of tree
    def use(self, input):
        for i in range(len(input)):  # checking if input is correct
            if input[i] != "0" and input[i] != "1":
                return -1

        if len(input) != self.variable_count:  # if input is incorrect
            return -2

        else:
            result = self._use(self.root, input)  # start traversing the tree
            if result != 1 and result != 0:
                return -3
            else:
                if result == 1:
                    return True
                else:
                    return False

    # function which traverses the tree recursivly
    def _use(self, current_node, direction):
        if current_node.variable_count==None:
            return current_node.function

        else:
            index = len(direction) - current_node.variable_count
            if direction[index] == "0" and current_node.left_child:
                return self._use(current_node.left_child, direction)
            elif direction[index] == "1" and current_node.right_child:
                return self._use(current_node.right_child, direction)


    # function which reduces current node if it was already created
    def reduce(self, node):
        if node is None:  # if we pass None do nothing
            return
        if self.used_nodes.get(node.function) is None:  # if node wasnt created add it to dictionary
            self.used_nodes[node.function] = node
            return node
        else:  # if node was created, return created node
            used_node = self.used_nodes.get(node.function)
            return used_node

    # function which checks if created node is redundant
    def check_redundant(self, node):
        try:
            if node.left_child == node.right_child:  # if pointers of node match
                return True
            return False
        except:
            return False

    # visualization of the tree without corrent pointer showcase
    # URL = https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right_child is None and node.left_child is None:
            line = '%s' % node.function
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left_child child.
        if node.right_child is None:
            lines, n, p, x = self._display_aux(node.left_child)
            s = '%s' % node.function
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right_child child.
        if node.left_child is None:
            lines, n, p, x = self._display_aux(node.right_child)
            s = '%s' % node.function
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left_child, n, p, x = self._display_aux(node.left_child)
        right_child, m, q, y = self._display_aux(node.right_child)
        s = '%s' % node.function
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left_child += [n * ' '] * (q - p)
        elif q < p:
            right_child += [m * ' '] * (p - q)
        zipped_lines = zip(left_child, right_child)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


