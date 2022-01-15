def past(h, m, s):
    h_ms = h * 3600000
    m_ms = m * 60000
    s_ms = s * 1000
    return h_ms + m_ms + s_ms


# Best Practices
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000