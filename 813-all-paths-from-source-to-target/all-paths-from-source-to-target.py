class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        d={}
        for i in range(len(graph)):
            d[i]=graph[i]
        # return d

        s=[[0,[0]]]
        l=[]
        while s:
            node,path=s.pop()

            if node==len(graph)-1:
                l.append(path)
            else:
                for i in d[node]:
                    s.append([i,path+[i]])
        return l























        
        