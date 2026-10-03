class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if strs == []:
            return [['']]

        lst = []
        map = {} # word (str) : index (int)
        count = 0

        for word in strs:
            srt = sorted(word)
            string = " ".join(srt)

            if string in map:
                i = map[string] # find index of anagrams
                lst[i].append(word) # add unsorted word to lst alongside it's anagrams
            else:
                map[string] = count # add anagram and location of it in list to map
                lst.append([word]) # add that anagram in a list of its own so others of its kind that are found can be added to same list
                count += 1 

        return lst



