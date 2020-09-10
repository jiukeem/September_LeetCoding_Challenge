class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        i = 0
        for s, g in zip(secret, guess):
            if s == g:
                a += 1
                secret = secret[:i] + secret[i + 1:]
                guess = guess[:i] + guess[i + 1:]
            else:
                i += 1

        secret = [s for s in secret]
        guess = [g for g in guess]

        b = 0
        for g in guess:
            if g in secret:
                b += 1
                secret.remove(g)

        return f'{a}A{b}B'
# Status: Accepted
# Algorithm:
# Time Complexity: O(n)
# Runtime: 76ms (top 80.5%)
# Intuitions: 처음 포문을 돌리면서 스트라이크를 찾고 그 숫자는 빼버린다.
#             그 다음 포문을 다시 돌리면서 (스트라이크의 가능성은 없으니) 해당 숫자가 secret안에 들었으면
#             b에 1을 추가해주면서 secret에서 그 숫자를 제거한다(중복으로 세지 않도록)
# Note: 포문 한번에 스트라이크와 볼을 동시에 처리할 수 있을까? 그리고 볼 탐색과정에서 secret에서 숫자를 제거해주기 위해
#       secret과 guess를 리스트로 변환해줬는데 이 과정도 생략할 방법이 있을까?


# leetcode discussion
from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = sum(s == g for s, g in zip(secret, guess))
        both = Counter(secret) & Counter(guess)
        return f'{a}A{sum(both.values()) - a}B'
# Status: Accepted
# Algorithm:
# Time Complexity: O(n)
# Runtime: 40ms (top 21.0%)
# Intuition: 스트라이크인 부분은 굳이 없애지 않고 전체에 대해 값을 구한 뒤 스트라이크를 빼는 방법
# Note: both 부분에서 & 연산자가 잘 이해되지 않는다.
#       return 부분의 코드로 추정해보건데 양쪽 counter의 교집합 counter를 반환하는 듯.