class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[pos, spd] for pos, spd in zip(position, speed)]

        for p, s in sorted(pair)[::-1]:
            time_to_target = (target - p) / s
            stack.append(time_to_target)
            # smaller time means getting to the target faster
            # but in fact no car can pass the one another
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # means they will get to target at the same time
                # even when stack[-1] car can come faster
                stack.pop()
        return len(stack)