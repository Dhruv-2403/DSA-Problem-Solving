class Solution:
    def checkStraightLine(self, l: List[List[int]]) -> bool:
        (x1,y1),(x2,y2)=l[0],l[1]
        for x3,y3 in l[2:]:
            
        
            if (y3-y2)*(x3-x1)!=(y3-y1)*(x3-x2):
                return False
        return True
                
