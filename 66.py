class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        digits[-1] += 1
        while digits[-1] == 10:
            res.insert(0,0)
            digits.pop()
            if  digits:
                digits[-1] += 1
            else:
                digits.append(1)
        while digits:
             res.insert(0,digits.pop())
        return res
    
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i]*pow(10, len(digits)-1-i)
        return [int(i) for i in str(num+1)]    

            
            
        