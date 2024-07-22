from keras.models import Sequential
from keras.utils import to_categorical
from keras.datasets import mnist
from keras.layers import Dense
from keras.optimizers import SGD, Adam
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint

#load dataset
(x_train,y_train), (x_test,y_test) = mnist.load_data()
print(x_train.shape)
x_train= x_train.reshape(x_train.shape[0],784)
x_test=x_test.reshape(x_test.shape[0],784)
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)
#print(type(y_train[0]))
#print(x_train.max())

#normalization
x_train=x_train/255
x_test=x_test/255
#print(x_train.max())
#print(x_train.min())

#configuration 1
model1=Sequential()
model1.add(Dense(100,input_dim=784,activation='relu'))
model1.add(Dense(10,activation='softmax'))
model1.compile(optimizer=SGD(learning_rate=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])

cb=ModelCheckpoint('myModel.keras',monitor='val_loss',save_best_only=True,mode="min")
#train model
obj_fit=model1.fit(x_train,y_train,epochs=10,batch_size=64,verbose=1,validation_split=0.2,callbacks=[cb])
plt.plot(obj_fit.history['val_loss'],label='val_loss')
plt.plot(obj_fit.history['loss'],label='train_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

A=model1.evaluate(x_test,y_test)
print(A[1])