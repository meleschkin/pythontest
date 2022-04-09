import numpy as np

print(np.__version__)

import scipy as sp

print(sp.__version__)

v_hor_np = np.array([1, 2])
print(v_hor_np)

v_hor_zeros_v1 = np.zeros((5,))
print(v_hor_zeros_v1)

v_hor_zeros_v2 = np.zeros((1, 5))
print(v_hor_zeros_v2)

v_hor_one_v1 = np.ones((5,))
print(v_hor_one_v1)

v_hor_one_v2 = np.ones((1, 5))
print(v_hor_one_v2)

v_vert_np = np.array([[1], [2]])
print(v_vert_np)

v_vert_zeros = np.zeros((5, 1))
print(v_vert_zeros)

v_vert_ones = np.ones((5, 1))
print(v_vert_ones)

m_sqr_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m_sqr_arr)

m_sqr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_sqr_arr1 = np.array(m_sqr)
print(m_sqr_arr1)

m_sqr_mx = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m_sqr_mx)

m_sqr_mx1 = np.matrix('1 2 3; 4 5 6; 7 8 9')
print(m_sqr_mx1)

m_diag = [[1, 0, 0], [0, 5, 0], [0, 0, 9]]
m_diag_np = np.matrix(m_diag)
print(m_diag_np)

m_sqr_mx = np.matrix('1 2 3; 4 5 6; 7 8 9')
diag = np.diag(m_sqr_mx)
print(diag)

m_diag_np = np.diag(np.diag(m_sqr_mx))
print(m_diag_np)

m_e = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m_e_np = np.matrix(m_e)
print(m_e_np)

m_eye = np.eye(3)
print(m_eye)

m_idnt = np.identity(3)
print(m_idnt)

m_zeros = np.zeros((3, 3))
print(m_zeros)
