class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        clips.sort()

        last_end, end, count = 0, 0, 0

        for c in clips:
            if c[0] > last_end:
                if c[0] <= end:
                    count += 1
                    last_end = end
                else:
                    return -1

            if end < c[1]:
                end = c[1]
            
            if end >= time:
                count += 1
                return count
        return -1    
