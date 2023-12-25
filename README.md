# Tree Visualization


### Task Summary

The goal is to create a visual representation of a tree in "UTF16-art." The tree is defined by a leaf containing values, and each internal node has a name and a list of children. The visualization follows specific rules, including top-down rendering, left-to-right orientation, and indentation based on node depth.

### Tree examples

**Valid Trees:**
- Trivial 1-node tree: `[1, []]`
- 1-node tree with reversed ID and children order: `[[], 2]`
- Trivial 3-node tree: `[1, [2, 3]]`

**Invalid Trees:**
- `None`
- `[]`
- `[666]`
- `[1, 2]`
- `(1, [2, 3])`

### Rendering Rules

- Rendering from top to bottom, left to right.
- Nodes represented by string serialization of their objects.
- Indentation based on node depth.
- Arrows indicate relationships between nodes.
- Arrow lengths determined by an indent value.
- Vertical lines connect child nodes at the arrow beginnings.

### Additional Requirements

- Raise an exception for invalid input: `raise Exception('Invalid tree')`.
- Follow PEP8 coding style.
- Use built-in methods only; no additional module imports.

### Example

```python
# Example 1
input_tree = [[[1, [True, ['abc', 'def']]], [2, [3.14159, 6.023e23]]], 42]
params = {'indent': 4, 'separator': '.'}
# Output:
# 42
# ├──>1
# │   └──>True
# │      
# │       ├──>abc
# │       └──>def
# └──>2
#     ├──>3.14159
#     └──>6.023e+23 
