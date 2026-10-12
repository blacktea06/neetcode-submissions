class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for word in strs:
            if word == "":
                encoded += f"0#" # empty string format eg. 0#
            else:
                encoded += f"{len(word)}#{word}" # format eg. 5#Hello
        # print(f"encoded: {encoded}")

        return f"{encoded}"
       

    def decode(self, s: str) -> List[str]:

        N = len(s)
        decoded = []
        length = -1
        i = 0

        while i < N:
            string = ""
            temp_length = ""

            #print(f"s[i]: {s[i]}")
            while s[i] != "#":
                temp_length += s[i]
                i += 1

            length = int(temp_length)

            i += 1 # move onto the string
            for _ in range(length):
                string += s[i]
                i += 1
            
            # print(i)

            decoded.append(string)

            # print(decoded)

        return decoded
            


                
            



        

                
                
                

            




        return None
        




        



        
        

        
