class Solution(object):
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        unit = 1
        roman = ""
        while num > 0:
            num, mod = divmod(num, 10)
            if unit == 1:
                roman = self.getRoman(mod,"I","V","X") + roman
                unit += 1
            elif unit == 2:
                roman = self.getRoman(mod,"X","L","C") + roman
                unit += 1
            elif unit == 3:
                roman = self.getRoman(mod,"C","D","M") + roman
                unit += 1
            elif unit == 4:
                roman = self.getRoman(mod,"M","V","") + roman
                
        return roman
    
    def getRoman(self, num, one, five, ten):
        retval = ""
        if num >= 1 and num <=3:
            for i in range(num):
                retval += one
        elif num == 4:
            retval = one + five
        elif num == 5:
            retval = five
        elif num >= 6 and num <= 8:
            num -= 5
            retval = five
            for i in range(num):
                retval += one
        elif num == 9:
            retval = one + ten
        
        return retval