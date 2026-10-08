# Questions :--- 297. Serialize and Deserialize Binary Tree

"""

Problem Statements :---

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

"""

# Code :--

from collections import deque

class Codec:
    # Serialize tree level by level using BFS
    def serialize(self, root, TreeNode):
        if not root:
            return ""
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                result.append("N")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(result)

    # Deserialize by pairing tokens as children of each dequeued node
    def deserialize(self, data, TreeNode):
        if not data:
            return None
        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(tokens):
            node = queue.popleft()
            # Left child
            if tokens[i] != "N":
                node.left = TreeNode(int(tokens[i]))
                queue.append(node.left)
            i += 1
            # Right child
            if i < len(tokens) and tokens[i] != "N":
                node.right = TreeNode(int(tokens[i]))
                queue.append(node.right)
            i += 1
        return root
