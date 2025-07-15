class Solution(object):
    def isValid(self, word):
        # if len(word)>=3:
        count_c=0
        count_v=0
        count_n=0
        for i in word:
            if i in ["a","A","e","E","i","I","O","o","u","U"]:
                count_v+=1
            elif i in ["0","1","2","3","4","5","6","7","8","9"]:
                count_n+=1
            else:
                count_c+=1
        # return count_v
        if word.isalnum() and len(word)>=3 and count_v>=1 and count_c>=1:
            return True
        return False


        