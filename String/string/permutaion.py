class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
  

        if len(s1) > len(s2):
            return False

        dict1 = {}
        dict2 = {}

        # Build frequency dictionaries
        for ch in s1:
            dict1[ch] = dict1.get(ch, 0) + 1

        k = len(s1)

        # Build the first window
        for i in range(k):
            dict2[s2[i]] = dict2.get(s2[i], 0) + 1

        if dict1 == dict2:
            return True

        # Slide the fixed-size window
        for right in range(k, len(s2)):

            # Remove outgoing character
            outgoing = s2[right - k]
            dict2[outgoing] -= 1

            if dict2[outgoing] == 0:
                del dict2[outgoing]

            
            incoming = s2[right]
            dict2[incoming] = dict2.get(incoming, 0) + 1

            if dict1 == dict2:
                return True

        return False
        