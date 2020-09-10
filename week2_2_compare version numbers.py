class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def trim(version):
            trim = list(map(int, version.split('.')))
            return trim

        def back_to_int(trimed_list):
            s = ''
            for num in trimed_list:
                s += str(num)
            return int(s)

        t1 = trim(version1)
        t2 = trim(version2)

        if len(t2) < len(t1):
            for _ in range(len(t1) - len(t2)):
                t2.append(0)
        if len(t1) < len(t2):
            for _ in range(len(t2) - len(t1)):
                t1.append(0)

        ver1 = back_to_int(t1)
        ver2 = back_to_int(t2)

        if ver2 < ver1:
            return 1
        elif ver1 < ver2:
            return -1
        else:
            return 0
# Status: Accepted
# Algorithm:
# Time Complexity: O(n)
# Runtime: 20ms (top 1.1%)