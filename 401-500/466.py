class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        for s in s2:
            if s not in s1:
                return 0
        i, j = 0, 0
        c1, c2 = 1, 0
        ret = [(0, 0)]
        vis = [[0] * len(s2) for i in range(len(s1))]
        end1, end2 = False, False
        while True:
            while s1[i] != s2[j]:
                i += 1
                if i == len(s1):
                    c1 += 1
                    i = 0
            if j == len(s2) - 1:
                c2 += 1
                # print(i,j,c1,c2)
                if ret[-1][0] == c1:
                    ret.pop()
                elif end2:
                    break
                ret.append((c1, c2))
                if end1:
                    end2 = True
            # print(i,j,c1,c2)
            if vis[i][j] == 0:
                vis[i][j] = 1
            else:
                end1 = True
            i, j = i + 1, j + 1
            if i == len(s1):
                c1 += 1
                i = 0
            if j == len(s2):
                j = 0
        # print(ret)
        k = 1
        if n1 <= ret[k][0]:
            for i in range(k, -1, -1):
                if n1 >= ret[i][0]:
                    return int(ret[i][1] / n2)
        else:
            n1 -= ret[k][0]
            ans = ret[k][1]
            c1, c2 = ret[-1][0] - ret[k][0], ret[-1][1] - ret[k][1]
            ans += c2 * int(n1 / c1)
            n1 = n1 % c1
            for i in range(len(ret) - 1, -1, -1):
                if n1 >= ret[i][0] - ret[k][0]:
                    ans += ret[i][1] - ret[k][1]
                    return int(ans / n2)
        return 0
