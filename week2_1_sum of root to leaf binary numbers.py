# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my solution
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, val):
            if node:
                val = (val << 1) | node.val
                if node.left is None and node.right is None:
                    self.ans += val
                    return
                else:
                    dfs(node.left, val)
                    dfs(node.right, val)

        dfs(root, 0)
        return self.ans
# Status: Accepted
# Algorithm: DFS
# Time Complexity: O(n)
# Runtime: 36ms (top 18.4%)
# Note: 예전에 풀었던 문제. 그 떄는 스택을 이용한 dfs로 풀었었는데 이번엔 재귀로 해봤다.
#       런타임이 좀 더 단축됐다.
#       처음에는 node가 None이 아닐 경우 self.ans를 업데이트 하고 left와 right에 대해서 dfs를 실행하는 방식으로 짰는데
#       그러면 leaf node에서의 val이 두 번 더해져서 잘못된 값이 출력된다. 조건문을 수정함