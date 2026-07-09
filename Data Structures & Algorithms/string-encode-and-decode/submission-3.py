class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg += s + "-"
        return msg

    def decode(self, s: str) -> List[str]:
        if s == "-":
            return [""]
        if s == "":
            return []
        s = s[:-1]
        strs = s.split("-")
        return strs