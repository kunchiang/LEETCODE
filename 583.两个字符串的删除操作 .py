# encoding:utf-8
class Solution:
    def minDistance(self, word1, word2):
        count = 0
        if not word1 or not word2:
            return count
        res = list()
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word1[j]:
                    res.append(word1[i])
        return len(res)


    def search(self, word1, word2):
        count = 0
        if not word1 or not word2:
            return count
        if word1[0] == word2[0]:
            count += 1
            count += self.search(word1[1:], word2[1:])
        else:
            count += max([self.search(word1[1:], word2[0:]), self.search(word1[0:], word2[1:])])
        return count
    def _minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        step = self.search(word1, word2)
        return len(word1)+len(word2)-2*step

w1 = "dphenylhydrazine"
w2 = "phenylhydrazine"

sol = Solution()
res = sol.minDistance(w1, w2)
print(res)