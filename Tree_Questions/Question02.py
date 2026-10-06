# Questions :---- 199. Binary Tree Right Side View

"""

Problem Statements :---

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:

Example 2:

Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
Explanation:


Example 3:

Input: root = [1,null,3]
Output: [1,3]

Example 4:

Input: root = []
Output: []

"""

# Code :----


def rightSideViwes(root):
    result = []

    def dfs(node, depth):
        if not node:
            return

        if depth == len(result):
            result.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return result

