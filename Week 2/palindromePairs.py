class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(check):
            return check == check[::-1]

        wordict = {}
        for i, word in enumerate(words):
            wordict[word] = i
        res = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, postfix = word[:j], word[j:]
                if is_palindrome(prefix):
                    back = postfix[::-1]
                    if back != word and back in wordict:
                        res.append([wordict[back], i])
                if j != len(word) and is_palindrome(postfix): # We only check j!=len(word) to avoid duplicates
                    back = prefix[::-1]
                    if back != word and back in wordict:
                        res.append([i, wordict[back]])
        return res
