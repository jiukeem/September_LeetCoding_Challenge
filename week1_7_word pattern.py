class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(pattern) == 0 or len(str) == 0:
            return False
        # 예외처리

        words = str.split()
        if len(words) != len(pattern):
            return False
        # 단어개수와 패턴길이가 다르면 False 출력

        table = {char: words[i] for i, char in enumerate(pattern)}
        # 일대일 딕셔너리 생성(만약 false case면 마지막 걸로 업데이트 되겠지)
        if len(set(table.values())) != len(table):
            return False
        # 서로 다른 키가 같은 벨류를 가지고 있을 경우 False 출력

        for i, char in enumerate(pattern):
            if words[i] != table[char]:
                return False
        # 패턴을 돌면서 딕셔너리의 키벨류쌍과 단어가 일치하는지 확인.
        # false case면 일치하지 않는 경우가 반드시 생긴다.

        return True
        # 이 모든 고난을 통과했다면 true case!
# Status: Accepted
# Algorithm: Hash Table
# Time Complexity: O(n)
# Runtime: 20ms (top 0.7%) 와우