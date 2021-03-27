def mul(x, y):
    n_x = int(len(str(x)))
    n_y = int(len(str(y)))
    d_x, m_x = divmod(n_x, 2)
    d_y, m_y = divmod(n_y, 2)
    if n_y == 1 or n_x == 1:
        return x * y
    else:
        a = int(str(x)[0:d_x + m_x])
        b = int(str(x)[d_x + m_x:])
        c = int(str(y)[0:d_y + m_y])
        d = int(str(y)[d_y + m_y:])
        ac = mul(a, c)
        bd = mul(b, d)
        pq = mul(a + b, c + d)
        abdc = pq - ac - bd
        return ac * pow(10, min(n_x, n_y)) + abdc * pow(10, int(max(n_x, n_y) / 2)) + bd


assert 5678 * 1234 == mul(5678, 1234), "Error, not equal"
