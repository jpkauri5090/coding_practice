

class Solution(object):
    def __init__(self, text):
        self.text = text

    def longest_substring_with_k_distinct_characters(self, k):
        maxLength = 0
        subString = []

        rightBar = 0

        while(rightBar < len(self.text)):

            if(len(set(subString)) <= 3):
                subString.append(self.text[rightBar])
                rightBar += 1
            else:
                subString.pop(0)
            
            if(len(set(subString)) == 3):
                maxLength = max(maxLength, len(subString))

        return maxLength

print Solution('aabcdefff').longest_substring_with_k_distinct_characters(3)
# 5 (because 'defff' has length 5 with 3 characters)