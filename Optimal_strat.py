def opti_strat(move_possible, best_strat=[], crt_opponent_pick=[], crt_player_pick=[]):
    l = [0, -1]
    if len(move_possible) == 0:
        if sum(crt_opponent_pick) < sum(crt_player_pick):
            best_strat = crt_player_pick.copy()
        return best_strat
    for i in l:
        crt_player_pick.append(move_possible[i])
        for j in l:
            crt_opponent_pick.append(move_possible[i + 1:len(move_possible) + i][j])
            best_strat = opti_strat(move_possible[i + j + 2:len(move_possible) + i + j],best_strat,crt_opponent_pick,crt_player_pick)
            crt_opponent_pick.pop()
        crt_player_pick.pop()
    return best_strat


L = [20, 30, 2, 2, 2, 10]
best_strat = opti_strat(L)
print(best_strat)
