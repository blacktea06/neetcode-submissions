class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2, longest_window = 0, 0, 0
        substring = set()

        while p2 < len(s): # {pw}
            if s[p2] in substring:
                substring.remove(s[p1])
                longest_window = max(longest_window, p2-p1)
                p1 += 1
            else:
                substring.add(s[p2])
                p2 += 1
        print(longest_window, len(substring))
        return max(longest_window, len(substring))

                

                    

        




        