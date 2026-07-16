class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs is None:
            return "None"
        string = ""
        for s in strs:
            string += s + "\r"
        #print(string)
        return string

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        #print(s.split(str(0xA)))
        return s.split("\r")[:-1]