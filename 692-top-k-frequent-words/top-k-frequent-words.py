
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d={}
        for i in words:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        


        heap=[]
        for i,j in d.items():
            heap.append((-j,i))
        heapq.heapify(heap)
        l=[]
        for i in range(k):
            l.append(heapq.heappop(heap)[1])
        return l
        

