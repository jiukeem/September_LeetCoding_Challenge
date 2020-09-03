# my solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(substring, s):
            if len(s) % len(substring) != 0:
                return False

            for i in range(len(s)):
                if s[i] != substring[i % len(substring)]:
                    return False
            return True

        substring = [s[0]]
        while len(substring) <= (len(s) // 2):
            for char in s[1:]:
                if char == substring[0]:
                    if check(substring, s) is True:
                        return True
                substring.append(char)

        return False
# Status: Accepted
# Time Complexity: O(n^2)
# Runtime: 356ms (top 87.6%)
# 간신히 타임아웃을 면한 수준이지만 그래도 나 혼자 짠 코드다. 뿌듯행


# leetcode discussion solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double_s = s + s
        if s in double_s[1:-1]:
            return True
        return False
# Status: Accepted
# Time Complexity: O(n)
# Runtime: 24ms (top 0.5%)
# 디스커션에 이런 풀이들이 잔뜩 있던데 도저히 반례를 못 찾겠지만서도 이해가 안가는 어벙벙한 풀이.
# 이게 도대체 왜 되는거지? 근데 아무리 반례를 들려고해도 없다. 
# 이런 방식으로 할 수 있다니 너무나 충격ㅠㅠ