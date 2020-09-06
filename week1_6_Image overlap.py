class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        res = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                overlap = 0
                for k, row in enumerate(A):
                    for l, ele in enumerate(row):
                        if ele == 1:
                            while B[k + i][l + j]:
                                if B[k + i][l + j] == 1:
                                    overlap += 1
                res = max(res, output)

        return res
# Status: Time Limit Exceeded
# Algorithm: Brute Force
# Time Complexity: O(n^4) (n = len(A))
# Runtime: 행렬너비가 최대 30인데 30은 커녕 n=3에서도 타임아웃이 걸린다.


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        pad_up = [[0] * (3 * n - 2) for _ in range(n - 1)]
        pad_down = [[0] * (3 * n - 2) for _ in range(n)]
        center = [[0] * (n - 1) + B[i] + [0] * n for i in range(len(B))]
        padded_B = pad_up + center + pad_down

        def convolution(M1, M2):
            height = len(M1)
            width = len(M1[0])
            overlap = 0
            for i in range(height):
                for j in range(width):
                    overlap += M1[i][j] * M2[i][j]
            return overlap

        res = 0
        for i in range(2 * n - 1):
            for j in range(2 * n - 1):
                overlap = convolution(A, padded_B[i:i + n][j:j + n])
                res = max(res, overlap)

        return res
# Status: Runtime error


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)

        def convolution(M1, M2, i, j):
            height = len(M1)
            width = len(M1[0])
            overlap = 0
            for k in range(height):
                for h in range(width):
                    while M1[k][h] and M2[k + i][h + j]:
                        overlap += M1[k][h] * M2[k + i][h + j]
            return overlap

        res = 0
        for i in range(1 - n, n):
            for j in range(1 - n, n):
                overlap = convolution(A, B, i, j)
                res = max(res, overlap)

        return res
# Status: Time Limit Exceeded
# 릿코드 솔루션도 결국은 for문을 네번 사용하는 O(n^4)인데 왜 내 답안은 timeout이 나고 릿코드 솔루션은 잘 돌아갈까?