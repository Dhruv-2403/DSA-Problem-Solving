class Solution(object):
    from collections import Counter
    def minCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype
        :int
        """

        d=Counter()
        d2=Counter()
        d3={}
        for i in nums1:
            if i not in d:
                d[i]=1
           
            else:
                d[i]+=1
               
        for i in nums2:
            if i not in d2:
                d2[i]=1
            # if i not in d3:
            #     d3[i]=1
            else:
                d2[i]+=1
                # d3[i]+=1
            
        
        if d==d2:
            return 0
        
        
            
        
        x0=0
        #     flag=True
        #     for i,j in d.items():
        #         count2=0
        #         if i in d2:
        #             flag=True
        #         if i not in d2:
        #             flag=False
        #         if i in d2:
        #             count2=d2[i]
        #             x0+=abs((j-count2))//2
        #         if (j+count2)%2!=0:
        #             return -1
        #         if i not in d2:
        #             count2=d[i]
        #             x0+=abs((j-count2))//2
        #         # print(count2)

        #     # return flag


            

        #     for i,j in d2.items():
        #         if flag:
        #             flag=False
        #             continue
        #         count1=0
        #         if i in d:
        #             count1=d[i]
        #             # x0+=abs(j)//2
                
                
        #         if (j+count1)%2!=0:
        #             return -1
                

        #         if i not in d:
        #             count1=d2[i]

        #             x0+=abs(j)//2
        #     return x0
        
        # return d3
        for i in set(nums1+nums2):
            if abs(d[i]-d2[i])%2==1:
                return -1
            x0+=abs(d[i]-d2[i])//2
        return x0//2
        #

        
        
    
        