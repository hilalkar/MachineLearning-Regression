
from numpy.linalg import pinv
from numpy.linalg import lstsq
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.python.ops.gen_candidate_sampling_ops import learned_unigram_candidate_sampler

V = np.array([[3,5,-9],[-8,-6,5],[10,3,-6]])
y = np.array([[-3],[10],[-8]])

print(V)
print(y)

c1 = np.linalg.dot(pinv(V),y) # pseudo-inverse yöntemi
print(c1)

print(np.dot(V,c1))
c2 = np.dot(np.dot(pinv(np.dot(V.T,V)),V.T),y) #en küçük kareler yöntemi
c3 = lstsq(V, y, rcond=None)[0]    #numpy ın lstsq fonk yöntemi

print(c2)
print(c3)
print(np.dot(V,c2))
print("-"*30)
print(np.dot(V,c3))

#
# Aşağıdaki doğrusal denklem sistemi verilmiştir:
#
#     3x + 5y - 9z = -3
#    -8x - 6y + 5z = 10
#     10x + 3y - 6z = -8
#
# Bu sistemi çözmek için üç farklı yöntem kullanarak bilinmeyenlerin (x, y, z) değerlerini hesaplayın. Python kullanarak bu hesaplamaları yapınız ve her bir yöntemin sonucunu karşılaştırınız.
#
# Psödo-ters (Pseudo-inverse) yöntemini kullanarak çözümü bulun.
# En Küçük Kareler Yöntemi (Least Squares) ile çözümü bulun.
# NumPy'nin lstsq fonksiyonunu kullanarak çözümü elde edin.

