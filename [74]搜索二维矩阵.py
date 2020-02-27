# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  示例 1: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false 
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def __bisearch(self, line, target):
        leng = len(line)
        if leng <= 0:
            return False
        elif leng <= 2:
            if target == line[0] or target == line[-1]:
                return True
            else:
                return False
        else:
            mid = int(leng/2)
            if target == line[mid]:
                return True
            elif target > line[mid]:
                return self.__bisearch(line[mid:], target)
            else:
                return self.__bisearch(line[:mid], target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or (len(matrix) == 1 and matrix[0] == []) or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        for line in matrix:
            if target == line[0] or target == line[-1]:
                return True
            elif target > line[0] and target < line[-1]:
                for i in line:
                    if target == i:
                        return True
        return False
# leetcode submit region end(Prohibit modification and deletion)


sol = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
matrix = []
target = 11
print(sol.searchMatrix(matrix, target))