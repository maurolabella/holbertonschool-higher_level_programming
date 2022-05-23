#!/usr/bin/python3
"""
Matrix multiplication - only Matrix product (two matrices)
Returns a new matrix
"""


def matrix_mul(m_a, m_b):
    """
    @m_a = a list of lists(matrix): integers or floats
    @m_b = a list of lists(matrix): integers or floats
    """
    msg_1_a = "m_a must be a list"
    msg_1_b = "m_b must be a list"
    msg_2_a = "m_a must be a list of lists"
    msg_2_b = "m_b must be a list of lists"
    msg_3_a = "m_a can't be empty "
    msg_3_b = "m_b can't be empty"
    msg_4_a = "m_a should contain only integers or floats"
    msg_4_b = "m_b should contain only integers or floats"
    msg_5_a = "each row of m_a must be of the same size"
    msg_5_b = "each row of m_b must be of the same size"
    msg_6 = "m_a and m_b can't be multiplied"

    equals = []
    if(m_a is None):
        raise ValueError(msg_3_a)
    if(m_b is None):
        raise ValueError(msg_3_b)
    if (m_a == [] or m_a == [[]]):
        raise ValueError(msg_3_a)
    if (m_b == [] or m_b == [[]]):
        raise ValueError(msg_3_b)
    if isinstance(m_a, (list)) is False:
        raise TypeError(msg_1_a)
    if isinstance(m_b, (list)) is False:
        raise TypeError(msg_1_b)
    if(len(set([len(row) for row in m_a])) > 1):
        raise TypeError(msg_5_a)
    if(len(set([len(row) for row in m_b])) > 1):
        raise TypeError(msg_5_b)
    if(len(m_a[0]) != len([1 for row in m_b])):
        raise ValueError(msg_6)
    for row in m_a:
        if isinstance(row, list) is False:
            raise TypeError(msg_2_a)
        for a in row:
            if isinstance(a, (int, float)) is False:
                raise TypeError(msg_4_a)
    for row in m_a:
        if isinstance(row, list) is False:
            raise TypeError(msg_2_a)
    for elem in row:
        if isinstance(elem, (int, float)) is False:
            raise TypeError(msg_4_a)
    for row in m_b:
        if isinstance(row, list) is False:
            raise TypeError(msg_2_b)
    for elem in row:
        if isinstance(elem, (int, float)) is False:
            raise TypeError(msg_4_b)
    equals = [[sum(a*b for a, b in zip(A_row, B_col))
               for B_col in zip(*m_b)] for A_row in m_a]
    return equals
