def render_tree(tree: list = None, indent: int = 2, separator: str = ' ') -> str:
    """
    Renders a tree structure as a string.

    Args:
        tree (list): The tree structure to be rendered.
        indent (int): The number of spaces to use for each level of indentation.
        separator (str): The separator to use between elements in the tree.

    Returns:
        str: The string representation of the rendered tree.

    Raises:
        Exception: If the tree is invalid or of an unsupported type.
    """
    if (tree is None) or isinstance(tree, tuple):
        raise ValueError('Invalid tree')

    output = ""
    type_layer, node = type_of_layer(tree)

    # [1, [...]]
    if type_layer == 1:
        tree.remove(node)
        output = output + str(node) + "\n"
        output += render_tree_inner(tree[0], indent, separator, "", (True, False))
    else:
        raise ValueError('Invalid tree')

    return output


# last_node indicates whether it is the last node (we need to print "├") or not (we need to print "└")
# follow indicates whether it is the last child (we need to print separator) or not (we need to print '│')
def render_tree_inner(tree: list = None, indent: int = 2, separator: str = ' ', separation: str = ' ', indicators: (bool, bool) = (False, False)) -> str:
    """
       Recursively renders a tree structure as a string with proper indentation and formatting.

       Args:
           tree (list): The tree structure to be rendered.
           indent (int): The number of spaces to use for each level of indentation.
           separator (str): The separator to use between elements in the tree.
           separation (str): The separation string to be used for indentation.
           indicators (bool, bool): First bool indicates whether the current node is the last one in its level, second
           indicates whether to add a vertical bar ('|') for vertical alignment.

       Returns:
           str: The string representation of the rendered tree.
       """
    output = ""
    type_layer, node = type_of_layer(tree)

    # [1, [...]]
    if type_layer == 1:
        output += separation
        if not indicators[0]:
            output += "├"
        else:
            output += "└"

        for _ in range(1, indent - 1):
            output += "─"

        output += ">" + str(node) + "\n"
        tree.remove(node)

        separation += '│' if indicators[1] else separator

        for _ in range(1, indent):
            separation += separator
        output += render_tree_inner(tree[0], indent, separator, separation, (True, False))
    # [1, 2, 3...] or [1]
    elif type_layer in (2, 4):
        output += separation
        if len(tree) == 1 and indicators[0]:
            output += "└"
        else:
            output += "├"

        for _ in range(1, indent - 1):
            output += "─"

        output += ">" + str(node) + "\n"
        tree.remove(node)

        output += render_tree_inner(tree, indent, separator, separation, (True, False))
    # [[],[],[]...]
    elif type_layer == 3:
        length = len(tree) - 1
        for i in range(0, length):
            output += render_tree_inner(tree[i], indent, separator, separation, (False, True))
        output += render_tree_inner(tree[length], indent, separator, separation, (True, False))

    return output


def type_of_layer(tree: list):
    """
    Determines the type of layer in a tree structure.

    Args:
        tree (list): The tree structure to analyze.

    Returns:
        tuple: A tuple containing the type of layer (int) and the identified node (str).
    """
    nums = 0
    lists = 0
    node = ""
    for elem in tree:
        if isinstance(elem, list):
            lists += 1
        else:
            nums += 1
            node = elem

    if nums == 1 and lists == 1:
        return 1, node
    if nums > 1 and lists == 0:
        return 2, tree[0]
    if nums == 0 and lists > 1:
        return 3, node
    if nums == 1 and lists == 0:
        return 4, node
    if nums == 0 and lists == 0:
        return 5, node
    raise ValueError('Invalid tree')
