#!/usr/bin/python3
"""
Matrix multiplication - only Matrix product (two matrices)
Returns a new matrix
"""
import numpy as np


class Not_Matrix_Imput(Exception):
    pass


class Matrix_Empty(Exception):
    pass


class NotInteger_NorFloat_Element(Exception):
    pass


class MultiplicationNotCompatibleMatrixes(Exception):
    pass


class ArgumentCompletionFault(Exception):
    pass


def lazy_matrix_mul(m_a, m_b):
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

    if(m_a is None):
        raise ArgumentCompletionFault(msg_3_a)
    if(m_b is None):
        raise ArgumentCompletionFault(msg_3_b)
    if (m_a == [] or m_a == [[]]):
        raise Matrix_Empty(msg_3_a)
    if (m_b == [] or m_b == [[]]):
        raise Matrix_Empty(msg_3_b)
    if isinstance(m_a, (list)) is False:
        raise Not_Matrix_Imput(msg_1_a)
    if isinstance(m_b, (list)) is False:
        raise Not_Matrix_Imput(msg_1_b)
    if(len(set([len(row) for row in m_a])) > 1):
        raise Not_Matrix_Imput(msg_5_a)
    if(len(set([len(row) for row in m_b])) > 1):
        raise Not_Matrix_Imput(msg_5_b)
    if(len(m_a[0]) != len([1 for row in m_b])):
        raise MultiplicationNotCompatibleMatrixes(msg_6)
    for row in m_a:
        if isinstance(row, list) is False:
            raise Not_Matrix_Imput(msg_2_a)
        for a in row:
            if isinstance(a, (int, float)) is False:
                raise NotInteger_NorFloat_Element(msg_4_a)
    for row in m_b:
        if isinstance(row, list) is False:
            raise Not_Matrix_Imput(msg_2_b)
        for b in row:
            if isinstance(b, (int, float)) is False:
                raise NotInteger_NorFloat_Element(msg_4_b)
    equals = np.dot(m_a, m_b)
    return equals
