class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        zipped = [list(x) + [(target - x[0]) / x[1]] + [0] for x in zip(position, speed)]
        order = sorted(zipped, key=lambda x: x[0])[::-1]
        print(order)

        while order[-1][0] < target:
            i = 0
            order_len = len(order)
            while i < order_len:
                #print(i, order[i])
                pos = order[i][0]
                speed = order[i][1]
                ttf = order[i][2]
                time_stamp = order[i][3]
                if pos >= target:
                    i += 1
                    continue

                new_pos = pos + speed
                if i > 0 and new_pos >= order[i-1][0] and (order[i-1][0] < target or (order[i-1][2] >= ttf and order[i-1][3] == time_stamp + 1)):
                    #print(order)
                    print(f"remove item, {order[i]}")
                    order.remove(order[i])
                    i -= 1
                    order_len -= 1
                else:
                    order[i] = [new_pos, speed, ttf, time_stamp + 1]
                    
                i += 1
                #print(order)
        print(order)
        return len(order)