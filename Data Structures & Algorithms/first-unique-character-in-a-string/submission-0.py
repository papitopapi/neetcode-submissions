class Solution:
    def firstUniqChar(self, s: str) -> int:

        # mapping ={}

        # for i in range(len(s)):
        #     if not s[i] in mapping:
        #         mapping[s[i]] = 1

        #     else:
        #         mapping[s[i]] += 1

        #     if mapping[s[i]] == 2:
        #         return i

        
        # return -1

        from collections import Counter

        s_counter = Counter(s)

        for key in s_counter:
            if s_counter[key] == 1:
                return s.index(key)


        return -1

        
        