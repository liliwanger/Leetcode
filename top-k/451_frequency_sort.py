class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
          
        bucket = [[] for _ in range(n+1)]
        for char, freq in count.items():
            bucket[freq].append(char)

        res = ""

        for i in range(n, 0, -1):
            for char in bucket[i]:
                res += char*i
        return res
