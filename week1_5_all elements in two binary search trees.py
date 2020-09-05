# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root, lst):
            if root:
                inorder(root.left, lst)
                lst.append(root.val)
                inorder(root.right, lst)

        from collections import deque
        lst1 = deque()
        lst2 = deque()
        inorder(root1, lst1)
        inorder(root2, lst2)

        res = []
        while lst1 and lst2:
            if lst1[0] < lst2[0]:
                res.append(lst1.popleft())
            else:
                res.append(lst2.popleft())

        res += lst1 or lst2
        return res
# Status: Accepted
# Algorithm: inorder search + merge sort
# Time Complexity: O(n)
# Runtime: 356ms (top 16.4%)
# Note: 이번 문제는 쉬웠다 보자마자 이렇게 풀면되겠다 생각이 들었다. 제일 기쁜건 난이도가 medium이라는거!
#       lst1과 lst2를 처음에 리스트로 해줬다가 데크로 바꿨는데 pop(0)에서 popleft()로 시간이 줄어들면서
#       runtime이 상위34프로에서 16프로로 올라갔다!