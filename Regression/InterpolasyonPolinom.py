 # verilen x ve y yi en az hata ile sağlayan 3.dereceden polinoma ait katsayıları bulma
 # x = [1,3,5,6,9,12,15]
 # y = [4,8,15,9,12,20,24]
 # vondermonde matrisi kullanarak en küçük kareler yöntemiyle çözünüz

import numpy as np
from numpy.linalg import lstsq

x = np.array([1, 3, 5, 6, 9, 12, 15])
y = np.array([4, 8, 15, 9, 12, 20, 24])

V = np.vander(x,4) #fonksiyonu, verilen x dizisini kullanarak bir Vandermonde matrisi oluşturur. Bu matriste her satır, polinomun kuvvetleri sırasıyla yazılır.
                   # 4 değeri sütun sayısını belirler (3.dereceden bir polinom 4 katsayı içerir

# En küçük kareler yöntemiyle katsayıları bulma
coefficients, _, _, _ = lstsq(V, y, rcond=None)
#lstsq 4 değer döndürür
#coefficients: En küçük kareler çözümündeki katsayıları içerir. Bu katsayılar, polinomu temsil eden katsayılardır.

print(" 3. dereceden polinomun katsayıları ", coefficients)