#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lens = len(s)
        mat = [['' for i in range(int(lens))] for j in range(numRows)]
        p = 0
        z = 0
        while p < lens:
            # 向下走 |
            for i in range(numRows):
                if p >= lens:
                    break
                # print(s[p])
                mat[i][z*numRows] = s[p]
                p += 1
            # 向右上走 /
            for j in range(1, numRows-1):
                if p >= lens:
                    break
                # print(s[p])
                mat[i-j][j+z*numRows] = s[p]
                p += 1
            z += 1
            if p >= lens:
                    break
        # for c in mat:
        #     print(c)
        return "".join(["".join(c) for c in mat])

sol = Solution()
s = 'LEETCODEISHIRING'
assert sol.convert(s, 3) == 'LCIRETOESIIGEDHN'
assert sol.convert(s, 4) == 'LDREOEIIECIHNTSG'
print(sol.convert('AB', 1))

