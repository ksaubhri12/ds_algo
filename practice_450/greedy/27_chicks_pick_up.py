def pick_up_chicks(positions: [], velocities: [], time: int, barn: int, min_chicks: int):
    n = len(positions)
    count = 0
    swap = 0
    not_possible = 0
    for i in reversed(range(0, n)):
        velocity = velocities[i]
        position = positions[i]
        distance_needed = barn - position
        distance_possible = velocity * time
        if distance_possible >= distance_needed:
            count = count + 1
            if not_possible > 0:
                swap = swap + not_possible

        else:
            not_possible = not_possible + 1

        if count >= min_chicks:
            break
    if count >= min_chicks:
        return swap

    else:
        return 'IMPOSSIBLE'


if __name__ == '__main__':
    pos = [0, 2, 3, 5, 7]
    vel = [2, 1, 1, 1, 4]
    t = 5
    k = 3
    ba = 10
    print(pick_up_chicks(pos, vel, t, ba, k))
    pos = [0, 2, 3, 4, 7]
    vel = [2, 1, 1, 1, 4]
    t = 5
    k = 3
    ba = 10
    print(pick_up_chicks(pos, vel, t, ba, k))
