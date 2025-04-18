class Solution:
    def countAndSay(self, n: int) -> str:
        # Base term: for n = 1, the sequence is "1"
        s = "1"
        
        # Build terms 2 through n by repeatedly run‑length‑encoding the previous
        for _ in range(1, n):
            s = self._rle(s)
        
        return s

    def _rle(self, s: str) -> str:

        # We'll build the encoded string piece by piece
        result = []
        
        # 'prev_char' is the digit under our current run, 'count' how many times in a row
        prev_char = s[0]
        count     = 1
        
        # Iterate over the string, starting from the second character
        for c in s[1:]:
            if c == prev_char:
                # Still in the same run?
                count += 1
            else:
                # Run ended: append "<count><prev_char>" to result
                result.append(str(count))
                result.append(prev_char)
                # Reset for the new character
                prev_char = c
                count     = 1
        
        # Append the final run after the loop
        result.append(str(count))
        result.append(prev_char)
        
        # Join all pieces into one string and return
        return "".join(result)
