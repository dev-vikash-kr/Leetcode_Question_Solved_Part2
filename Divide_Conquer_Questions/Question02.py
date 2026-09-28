# Questions :-- 427.Construct Quad Tree
"""
Problem Statements :----
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

Example : 1
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo

"""

# Code :---


def construct(self, grid, Node):
    def build(row, col, size):
        if size == 1:
            return Node(grid[row][col] == 1, True)

        half = size // 2
        top_left = build(row, col, half)
        top_right = build(row, col + half, half)
        bottom_left = build(row, half, col, half)
        bottom_right = build(row, half, col + half, half)

        # if(top_left.isLeaf and top top_right and bottom_left.isLeaf  )
        if (
            top_left.isLeaf
            and top_right.isLeaf
            and bottom_left.isLeaf
            and bottom_right.isLeaf
            and top_left.val == top_right.val == bottom_left.val == bottom_right.val
        ):
            return Node(top_left.val, True)

        return Node(True, False, top_left, top_right, bottom_left, bottom_right)

    return build(0, 0, len(grid))


grid = [[0, 1], [1, 0]]
print(construct(grid))
