# 내 풀이
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        from itertools import permutations
        max_time = -1

        for i, j ,k, l in permutations(A):
            if 10 * i + j < 24 and 10 * k + l < 60:
                max_time = max(max_time, 1000 * i + 100 * j + 10 * k + l)

        if max_time == -1:
            return ''

        return '%02d:%02d' % (max_time // 100, max_time % 100)
# 시간/공간복잡도 O(1). 이게 워낙 작은 인풋을 사용해서 그런지 36ms(상위40프로)에서 56ms(하위20프로)로 전체 범위가 좁다.
# 리스트 길이가 4로 고정이니 순열을 사용하고 싶은데 만들어내기가 어려워서 구글링 했더니 파이썬 내부에서 permutations를 지원하더라
# 마찬가지로 조합(combinations)도 intertools에서 지원함
# 스트링 출력 형식도 까먹어서 구글링했다.


# 릿코드 솔루션1
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = -1

        for h, i, j, k in itertools.permutaion(A):
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)

        if max_time == -1:
            return ''
        else:
            return '{:02d}:{:02d}'.format(max_time // 60, max_time % 60)
# 내꺼랑 같은 방법 오예! hour에 60을 곱하는 부분만 다른데 내 방식도 틀린건 아니지만 아무래도 시간이다보니 60으로 하는게 더 흐름이 자연스럽다.


# 릿코드 솔루션2 - permutation 직접 구현
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        max_time = -1

        def build_time(permutation):
            nonlocal max_time

            h, i, j, k = permutation
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)

        def swap(array, i, j):
            if i != j:
                array[i], array[j] = array[j], array[i]

        def permutate(array, start):
            if start == len(array):
                build_time(array)
                return

            for index in range(start, len(array)):
                swap(array, index, start)
                # repeat the permutation with the original array mutated
                permutate(array, start+1)
                swap(array, index, start)

        permutate(A, 0)
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)


# permutation 을 직접 구현해보자
class Solution:
    def largestTimeFromDigits(self, A):
        def gen_perm(list, start, perm_list):
            if start == len(list) - 1:
                perm_list.append(list)
                return

            for i in range(start, len(list)):
                list[start], list[i] = list[i], list[start]
                gen_perm(list, start+1, perm_list)
                list[start], list[i] = list[i], list[start]

        perm_list = []
        gen_perm(A, 0, perm_list)
        return perm_list
# 재귀함수로 순열을 만드는 함수를 짰는데 print하면 제대로 나오지만
# print(list) 대신 perm_list.append(list) 한 뒤에 perm_list를 출력하면
# 기본 리스트 24개가 들어가있다...
# 구글링을 해봐도 출력하는 방법밖에 안나와있고 저장해서 가져갈 수 있는 방법은 못찾겠다.
# 심지어 릿코드 솔루션도 순열리스트 한개를 만들 때마다 build_time을 실행한다
