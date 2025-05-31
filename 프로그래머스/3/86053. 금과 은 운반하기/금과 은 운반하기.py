def solution(a, b, g, s, w, t):
    left = 0
    right = 10**15  

    answer = right

    while left <= right:
        mid = (left + right) // 2
        total_gold = 0
        total_silver = 0
        total_weight = 0

        for i in range(len(g)):
            max_trips = mid // (t[i] * 2)
            if mid % (t[i] * 2) >= t[i]:
                max_trips += 1  

            max_move = max_trips * w[i]
            gold_movable = min(g[i], max_move)
            silver_movable = min(s[i], max_move)
            total_movable = min(g[i] + s[i], max_move)

            total_gold += gold_movable
            total_silver += silver_movable
            total_weight += total_movable

        if total_gold >= a and total_silver >= b and total_weight >= a + b:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer