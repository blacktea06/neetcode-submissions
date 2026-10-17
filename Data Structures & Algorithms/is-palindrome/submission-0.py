class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(c.lower() for c in s if c.isalnum()) # gets a string of only lowercase alphnumeric char
        N = len(s)
        j = N-1

        for i in range(N):
            print(f"At index i and j: s[{i}] = {s[i]} s[{j}] = {s[j]}")

            if s[i] != s[j]:
                return False
            j -= 1
        
        return True



        