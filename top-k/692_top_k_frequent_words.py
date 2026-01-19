class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        
        n = len(words)
        bucket = [[] for _ in range(n+1)]

        for word, fre in count.items():
            bucket[fre].append(word)

        res = []
        for i in range(n, 0 ,-1):
            # if not bucket[i]:
            #     continue
            bucket[i].sort()
            for item in bucket[i]:
                res.append(item)
                if len(res) == k:
                    return res
        return res
