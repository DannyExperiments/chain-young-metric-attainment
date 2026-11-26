"""Exact comparison of fixed-grid edit paths and run transport on finite inputs."""

from fractions import Fraction as Q
from heapq import heappop, heappush
from itertools import permutations, product


def run_indices(word):
    indices = []
    letters = []
    for letter in word:
        if not letters or letter != letters[-1]:
            letters.append(letter)
        indices.append(len(letters) - 1)
    return indices, letters


def transport_cost(source, target, distance, h):
    """Enumerate token destinations and evaluate only the resulting run counts."""
    u_runs, u_letters = run_indices(source)
    v_runs, v_letters = run_indices(target)
    costs = []
    for destination in permutations(range(len(source))):
        counts = {}
        for i, j in enumerate(destination):
            cell = (u_runs[i], v_runs[j])
            counts[cell] = counts.get(cell, 0) + 1
        relabel = sum(h * count * distance[u_letters[i]][v_letters[j]] for (i, j), count in counts.items())
        crossings = sum(
            first * second
            for (i, j), first in counts.items()
            for (k, l), second in counts.items()
            if i < k and j > l
        )
        costs.append(relabel + h * h * crossings)
    return min(costs)


def neighbors(word, distance, h):
    for i, letter in enumerate(word):
        for other in range(len(distance)):
            if letter != other:
                changed = word[:i] + (other,) + word[i + 1:]
                yield changed, h * distance[letter][other]
        if i + 1 < len(word) and letter != word[i + 1]:
            changed = word[:i] + (word[i + 1], letter) + word[i + 2:]
            yield changed, h * h


def edit_distances(source, distance, h):
    best = {source: Q(0)}
    frontier = [(Q(0), source)]
    while frontier:
        cost, word = heappop(frontier)
        if best[word] != cost:
            continue
        for changed, move_cost in neighbors(word, distance, h):
            candidate = cost + move_cost
            if changed not in best or candidate < best[changed]:
                best[changed] = candidate
                heappush(frontier, (candidate, changed))
    return best


def check_family(distance, max_cells, length=Q(1)):
    count = 0
    for n in range(1, max_cells + 1):
        h = length / n
        words = list(product(range(len(distance)), repeat=n))
        for source in words:
            costs = edit_distances(source, distance, h)
            assert len(costs) == len(words)
            for target in words:
                assert transport_cost(source, target, distance, h) == costs[target]
                count += 1
    return count


def check_two_letter_example(distance):
    # At d=1/3, t=1/3. The untouched blocks are 1/3, the recolored blocks 1/6.
    half = Q(1, 2)
    sixth = Q(1, 6)
    d = distance[0][1]
    assert d == Q(1, 3)
    assert edit_distances((0, 1), distance, half)[(1, 0)] == Q(1, 4)
    word = (0, 0, 0, 1, 1, 1)
    target = (1, 1, 1, 0, 0, 0)
    after_pushes = (1,) + word[1:-1] + (0,)
    first, second = after_pushes[1:3], after_pushes[3:5]
    assert first == (0, 0) and second == (1, 1)
    after_swap = after_pushes[:1] + second + first + after_pushes[5:]
    assert after_swap == target
    certified_cost = 2 * sixth * d + (2 * sixth) ** 2
    assert certified_cost == d - d ** 2 == Q(2, 9)
    assert edit_distances(word, distance, sixth)[target] == certified_cost
    assert transport_cost(word, target, distance, sixth) == certified_cost


def main():
    binary = ((0, Q(1, 3)), (Q(1, 3), 0))
    ternary = ((0, Q(1, 3), Q(1, 2)), (Q(1, 3), 0, Q(1, 4)), (Q(1, 2), Q(1, 4), 0))
    total_binary = check_family(binary, max_cells=4)
    total_ternary = check_family(ternary, max_cells=3)
    total_nonunit = check_family(binary, max_cells=3, length=Q(3, 2))
    check_two_letter_example(binary)
    assert (total_binary, total_ternary, total_nonunit) == (340, 819, 84)
    print(f"Binary alphabet, unit length: {total_binary} exact edit-path / transport comparisons.")
    print(f"Ternary rational metric, unit length: {total_ternary} exact comparisons.")
    print(f"Binary alphabet, length 3/2: {total_nonunit} exact comparisons.")
    print("AB to BA at distance 1/3: half grid optimum 1/4, sixth grid optimum 2/9.")
    print("Two 1/6 pushes and one 1/3 block swap realize the analytical optimum 2/9.")
    print("All finite checks passed.")


if __name__ == "__main__":
    main()
