def solution(players, m, k):
    answer = 0
    servers = []

    for player in players:
        if player >= m:
            cur_capa = sum(capa for capa, time in servers if time > 0)
            needed_capa = m * (player // m) - cur_capa

            if needed_capa > 0:
                servers.append([needed_capa, k])
                answer += needed_capa // m

        servers = [[capa, time - 1] for capa, time in servers if time > 1]

    return answer