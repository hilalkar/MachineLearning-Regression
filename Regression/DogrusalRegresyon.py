from traceback import print_tb

#Verilen doğrusal denklem sistemini, matris tersi ve en küçük kareler yöntemi ile çözerek katsayıları bulup sonuçları karşılaştıran bir Python kodu

import numpy as np
a = np.array([[3,5,-9],[-8,-6,5],[10,3,-6]])  #, 3x3 boyutunda bir matristir ve doğrusal denklem sistemindeki katsayıları içerir.
b = np.array([[-3],[10],[-8]])          # 3x1 boyutunda bir vektördür ve doğrusal denklem sistemindeki sonuçları içerir. a.c=b



#1. yöntem matrisin tersi ile çözüm
c=np.dot(np.linalg.inv(a),b)     #np.dot(np.linalg.inv(a), b), a matrisinin tersiyle b matrisini çarparak c katsayılarını bulur.
print("katsayılar ")
print(c)                       #Bu yöntem, a matrisinin kare bir matris olup tersinin alınabilir olduğu durumlarda kullanılabilir




# 2. Yöntem: En Küçük Kareler Yöntemi ile Çözüm
c2=np.linalg.lstsq(a,b,rcond=None)[0]
print("en küçük kareler yöntemi katsayısı ")
print(c2)


# Çözümlerin Karşılaştırılması
print("-"*50)
print("tahmin:")
print(np.dot(a,c))
print(" en küçük kareler yönteminin tahmini")   # Çıktılardaki sonuçlar b'ye ne kadar yakınsa, çözümün doğruluğu o kadar yüksektir.
print(np.dot(a,c2))
