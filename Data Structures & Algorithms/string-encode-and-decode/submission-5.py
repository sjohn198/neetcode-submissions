class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += s + "\r"
        #print(string)
        return string

    def decode(self, s: str) -> List[str]:
        #print(s.split(str(0xA)))
        return s.split("\r")[:-1]