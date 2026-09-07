class Solution:
    def compress(self, chars: List[str]) -> int:
        charLen = []
        i = 0
        val = []

        while i < len(chars):
            count = 0
            current = chars[i]

            while i < len(chars) and chars[i] == current:
                count += 1
                i += 1
                val = current

            if count > 1:
                charLen.extend([val] + list(str(count)))
            elif count == 1:
                charLen.append(val)

        chars[:] = charLen

        return len(chars)