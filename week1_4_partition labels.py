# leetcode solution
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {char: idx for idx, char in enumerate(S)}

        ans = []
        j = anchor = 0
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(j - anchor + 1)
                anchor = i + 1

        return ans
# Status: Accepted
# Algorithm: Greedy(kind of..?)
# Time Complexity: O(n)
# Runtime: 44ms (top 9.8%)

# 릿코드 챌린지는 내가 푸는게 아니라 답지를 보고 배워가는 느낌이 되어버렸다..ㅋㅋ
# 딕셔너리컴프리헨션이 똑똑하다. 저렇게 하면 같은 알파벳이 나올 때 value가 없데이트 되면서 마지막 위치가 저장된다.
# 아주 조금이지만 점점 더 간결하게 생각하는 실력이 늘고 있는 것 같다.
# 그 간결한 걸 짤 수 있지는 않지만 코드를 짜다보면 아 여기를 이 코드보다 더 깔끔하고 짧게 짤 수 있을거 같은데? 하는 느낌이 든다
# 혹은 아 이 부분에서 이걸 다 저장할 필요가 없을거 같은데? 하는 느낌들들# 지금은 그정도로 만족ㅎ//ㅎ