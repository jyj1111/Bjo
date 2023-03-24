def solution(cap, n, deliveries, pickups):
    answer=0
    deli=deliveries[::-1]
    pick=pickups[::-1]
    must_deli=0
    must_pick=0
    for i in range(n):
        must_deli+=deli[i]
        must_pick+=pick[i]
        while must_deli>0 or must_pick>0:
            must_deli-=cap
            must_pick-=cap
            answer+=(n-i)*2
    return answer