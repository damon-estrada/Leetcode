from queue import PriorityQueue

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        prio_que = PriorityQueue()
        # put everything in the prio queque
        # everything is multiplied by -1 going in and out in order to make it go from max to min
        for x in stones:
            x = x * -1
            prio_que.put(x)

        while prio_que.qsize() > 1:
            y = prio_que.get() * -1
            x = prio_que.get() * -1

            if y != x:
                y = (y - x) * -1
                prio_que.put(y)

        if prio_que.qsize() == 1:
            return prio_que.get() * -1
        else:
            return 0