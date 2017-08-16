class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon)
        m = len(dungeon[0])
        dp_prev = [[] for i in range(m)]
        dp_next = [[] for i in range(m)]
        dp_prev[0].append((dungeon[0][0], dungeon[0][0]))
        for i in range(1, m):
            prev, peak = dp_prev[i-1][0]
            val = prev+dungeon[0][i]
            dp_prev[i].append((val, min(peak, val)))
        for i in range(1, n):
            prev, peak = dp_prev[0][0]
            val = prev+dungeon[i][0]
            dp_next[0].append((val, min(peak, val)))
            for j in range(1, m):
                x, y = 0, 0
                arrx, arry, arrz = dp_prev[j], dp_next[j-1], dp_next[j]
                while x < len(arrx) and y < len(arry):
                    if arrx[x][0] == arry[y][0]:
                        if arrx[x][1] >= arry[y][1]:
                            val = arrx[x][0] + dungeon[i][j]
                            arrz.append((val, min(arrx[x][1], val)))
                        else:
                            val = arry[y][0] + dungeon[i][j]
                            arrz.append((val, min(arry[y][1], val)))
                        x += 1
                        y += 1
                    elif arrx[x][0] > arry[y][0]:
                        val = arrx[x][0] + dungeon[i][j]
                        arrz.append((val, min(arrx[x][1], val)))
                        if arrx[x][1] >= arry[y][1]:
                            y += 1
                        x += 1
                    else:
                        val = arry[y][0] + dungeon[i][j]
                        arrz.append((val, min(arry[y][1], val)))
                        if arrx[x][1] <= arry[y][1]:
                            x += 1
                        y += 1
                while x < len(arrx) and arrx[x][1] > arrz[-1][1]:
                    val = arrx[x][0] + dungeon[i][j]
                    arrz.append((val, min(arrx[x][1], val)))
                    x += 1
                while y < len(arry) and arry[y][1] > arrz[-1][1]:
                    val = arry[y][0] + dungeon[i][j]
                    arrz.append((val, min(arry[y][1], val)))
                    y += 1
            dp_prev = dp_next
            dp_next = [[] for j in range(m)]
        return 1 - min(0, max(map(lambda x:x[1], dp_prev[-1])))
                        
