class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        from collections import deque


        adj=[[] for _ in range(numCourses)]
        indeg=[0] * numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indeg[u]+=1
        # return adj

        q=deque([i for i in range(numCourses) if indeg[i]==0 ])
        
            
        count=0
        while q:
            course=q.popleft()








            count+=1
            for i in adj[course]:
                indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
        return count==numCourses




            




            




        












        

        