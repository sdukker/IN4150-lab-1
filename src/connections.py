def calc_connections(id: int, n, k) -> list:
    """
    Args:
        id: node-id
        n: amount of nodes
        k: number of desired connections per node
    """
    if k < 2:
        raise Exception("K must be larger or equal to 2")

    res = []

    if k % 2 != 0:
        if n%2 != 0:
            raise Exception("When K is odd, N must be even.")
        res.append((id + int(n/2) ) % n)

    for i in range(1, int(k/2)+1):
        res.append((id - i) % n)
        res.append((id + i) % n)

    return res


if __name__ == "__main__":
    N = 8
    K = 3
    for x in range(N):
        print(f"node {x}: {calc_connections(x, N, K)}")
