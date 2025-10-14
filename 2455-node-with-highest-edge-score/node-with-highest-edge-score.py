class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        # return edges
        ans=[0]*(len(edges))
        for i in range(len(edges)):
            ans[edges[i]]+=i
        # return ans
        return ans.index(max(ans))
        
