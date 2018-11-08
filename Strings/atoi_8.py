class Solution(object):
    def letter_range(self, s):
        if ((ord(s) >= 65 and ord(s) <= 90) or (ord(s) >= 97 and ord(s) <= 122)):
            return True
        return False
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        length = len(str)
        count_signs = 0
        seen_sign = False
        seen_number = False
        seen_letter = False
        build_number = ""
        for i in range(length):
            if str[i] == " ":
                if not seen_number and not seen_sign:
                    continue
                break
                
            if str[i] =="+" or str[i] == "-":
                if seen_sign:
                    break
                if seen_number:
                    break
                build_number += str[i]
                seen_sign = True
                count_signs += 1
            
            if ord(str[i]) >= 48 and ord(str[i]) <= 57:
                seen_number = True
                build_number += str[i]
            
            if self.letter_range(str[i]):
                if not seen_number:
                    return 0
                seen_letter = True
                break 
            
            if str[i] == ".":
                break
    
        if count_signs > 1:
            return 0
        if seen_sign and not seen_number:
            return 0
        
        if build_number == "" or build_number == "+" or build_number == "-":
            return 0
        
        if int(build_number) > 2147483647:
            return 2147483647
        
        elif int(build_number) < -2147483647:
            return -2147483648
        
        return int(build_number)
                
            
        
