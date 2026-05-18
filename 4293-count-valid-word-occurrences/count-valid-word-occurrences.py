from collections import Counter
class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s="".join(chunks).replace("--"," ").replace("- "," ").replace(" -"," ").strip("-").split()
        # return s
        d=Counter(s)
        # return d
        l=[]
        for i in queries:
            if i in d:
                l.append(d[i])
            else:
                l.append(0)
        return l

        