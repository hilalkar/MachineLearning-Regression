import numpy as np

a = np.array([[3,5,-9],[-8,-6,5],[10,3,-6]])  # Bu matris, denklemin katsayılarını temsil eder.
b = np.array([[-3],[10],[-8]])   # 3x1 boyutunda bir sütun vektörüdür. Bu vektör, denklemin sağ tarafındaki değerleri temsil eder.
c = np.dot(np.linalg.pinv(a),b)
print(c)  #sırasıyla sütun olarak x,y,z değerlerini yazdırır

#np.linalg.pinv(a), a matrisinin Moore-Penrose genel tersini (pseudo-inverse) hesaplar.
# np.dot(...) fonksiyonu, iki matrisin çarpımını hesaplar.
# Burada, a matrisinin genel tersi ile b sütun vektörünün çarpımını alıyoruz.
# Bu işlem, Ax = b şeklindeki bir denklemi çözmek için kullanılır ve sonuç c değişkenine atanır




# Soru:
# Doğrusal Denklem Çözümü: En Küçük Kareler Yöntemi
# Aşağıdaki doğrusal denklem sistemi verilmiştir:
#
#    3x + 5y - 9z = -3
#    -8x - 6y + 5z = 10
#    10x + 3y - 6z = -8
#
# Bu sistemi çözmek için En Küçük Kareler (Least Squares) yöntemini kullanarak,
# bilinmeyenlerin (x, y, z) değerlerini hesaplayın.
