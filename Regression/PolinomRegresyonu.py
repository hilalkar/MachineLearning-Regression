import numpy as np
from sklearn.metrics import r2_score
# bu kod, polinom regresyonunu çözmek ve modelin doğruluğunu değerlendirmek için kullanılan bir örnektir
# Verilen doğrusal denklemler için katsayıları, matrisin tersi ve en küçük kareler yöntemi ile hesaplayın.
# Ayrıca, 4. dereceden polinom regresyonu uygulayın, modelin doğruluğunu değerlendirin
# ve yeni bir gözlem için tahmin yapın. Modelin başarısını R² skoru ile ölçün ve sonuçları görselleştirin.

a=np.array([[3,5,-9],[-8,-6,5],[10,3,-6]])
b= np.array([[-3],[10],[-8]])

c=np.dot(np.linalg.inv(a),b)
print('Coefficients:')
print(c)

c2=np.linalg.lstsq(a,b,rcond=None)[0]
print('Coefficients of Least Square method:')
print(c2)
print('-'*50)
print('Predict:')
print(np.dot(a,c))
print('Predict of Least Square method:')
print(np.dot(a,c2))

#x=np.array([[1.0,2.7,3.2,4.8,5.6]])
x=np.array([[1,3,5,6,9,12,15]])
x=x.T
print(x.shape)
#y=np.array([22.0,17.8,14.2,38.3,51.7])
y=np.array([4,8,15,9,12,20,24])
y=y[:,np.newaxis]
print(y.shape)

V=np.concatenate([x**4,x**3,x**2,x,np.ones((x.shape[0],1))],axis=1)
print(V)
c=np.linalg.lstsq(V,y,rcond=None)[0]
print(c)

tahmin=np.dot(V,c)
print(np.concatenate((y,tahmin),axis=1))

x2=np.array([[3.8]])
V2=np.concatenate((x2**4,x2**3,x2**2,x2,np.ones((x2.shape[0],1))),axis=1)
tahmin2=np.dot(V2,c)

x3=np.arange(np.min(x),np.max(x),0.01)
x3=x3[:,np.newaxis]
#print(x3.shape)
V3=np.concatenate((x3**4,x3**3,x3**2,x3,np.ones((x3.shape[0],1))),axis=1)
tahmin3=np.dot(V3,c)

import matplotlib.pyplot as plt
plt.plot(x,y,marker='o')
plt.plot(x,tahmin,marker='.')
plt.plot(x2,tahmin2,marker='d')
plt.plot(x3,tahmin3)
plt.legend(['orjinal','tahmin','tahmin2','tahmin eğrisi'])
plt.show()

print('r2 score= ',r2_score(y,tahmin))