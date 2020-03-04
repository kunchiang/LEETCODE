#
# @lc app=leetcode.cn id=1362 lang=python3
#
# [1362] 最接近的因数
#

# @lc code=start
class Solution:
    def closestDivisors(self, num: int):# -> List[int]:
        # 797442477 超时
        import math
        i = int(math.sqrt(num+2))
        j = int(math.sqrt(num+2))
        while True:
            if i*j == num+1 or i*j == num+2:
                break
            elif i*j > num+2 and i > 1:
                i -= max(1, int((i*j - num-2)/j))
            elif i*j < num+1 and j < num+1:
                j += max(1, int((num+1 - i*j)/i))
                # j += 1超时，加上max之后ac
                # print(i, j)
        return [i, j]

# sol = Solution()
# print(sol.closestDivisors(797442477))

# @lc code=end

