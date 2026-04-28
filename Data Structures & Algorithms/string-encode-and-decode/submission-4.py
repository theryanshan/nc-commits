class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        output = []
        i, j = 0, 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j+1:j+1+length])
            i = j + 1 + length
            j = i
        return output