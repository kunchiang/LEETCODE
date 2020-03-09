#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    """
    关键：第一位为1的有(n-1)!个，也就是前1~(n-1)!个都是1开头的，
         通过比较当前位i和(n-i)!的大小关系判断当前位应该为几。

    思路：逐位确定，先确定第一位，再确定第二位...
        第一位：比较k与(n-1)!的大小
            若 k<(n-1)!，则第一位为1，将1从候选列表(nums)中删除
            若 k=(n-1)!，则第一位也为1，将1从候选列表(nums)中删除
            若 k<(n-1)!，则第一位肯定大于1，
                此时我们将k-=(n-1)!，并重复上述判断，判断第一位是否为2、3...
                直到判断成功
        然后判断第二位，比较k与(n-2)!的大小
        然后第三位
        ...
    需要注意的是，k是变化的，仅仅在开始时表示第几个位置，后面则表示还需要前进多少位
    """
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return '1'
        cl_ = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        nums = [str(i) for i in range(1, n+1)]
        res = ''
        cur = k
        for i in range(1, n+1):
            tmp = 0
            while True:
                if cur < cl_[n-i]:
                    res += nums[tmp]
                    nums.remove(nums[tmp])
                    break
                elif cur == cl_[n-i]:
                    # cur -= cl_[n-i] # 这是关键，这里不能减
                    res += nums[tmp]
                    nums.remove(nums[tmp])
                    break
                elif cl_[n-i] == 0:
                    # 这个判断也是关键，表示剩余候选词只剩一个了，
                    # 需要停止循环并直接添加到结果字符串
                    res += nums[0]
                    break
                else:
                    tmp += 1
                    cur -= cl_[n-i]
        return res

    ## 搞不来dfs
    def _getPermutation(self, n, k):
        nums_jc = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        nums = [str(i) for i in range(1, n+1)]
        def find(cur, res, i, last_nums):
            print(cur, res, i, last_nums)
            if cur == k:
                print("cur == (n-i)!")
                res += nums[i]
                return res
            if cur > k:
                print("cur > (n-i)!", cur, nums_jc[n-i-1])
                cur += nums_jc[n-i-1]
                find(cur, res, i+1, last_nums)
            if cur < k:
                print("cur < (n-i)!", cur, nums_jc[n-i-1])
                cur += nums_jc[n-i-1]
                res += nums[i]
                last_nums.remove(nums[i])
                find(cur, res, i-1, last_nums)
        res = find(1, '', 0, nums)
        return res

# sol = Solution()
# print(sol.getPermutation(4, 3))

# @lc code=end

