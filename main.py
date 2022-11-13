from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

model=load_model('chest_xray.h5')

img=image.load_img(r'.\test\NORMAL\IM-0001-0001.jpeg',target_size=(224,224))
x=image.img_to_array(img)
x=np.expand_dims(x, axis=0)
img_data=preprocess_input(x)
classes=model.predict(img_data)
print(classes)
print(classes[0])
result=int(classes[0][0])
if result==0:
    print("Person is Affected By PNEUMONIA")
else:
    print("Result is Normal")
# img=image.load_img(r'/content/drive/MyDrive/Colab Notebooks/test/PNEUMONIA/person88_bacteria_439.jpeg',target_size=(224,224))
# x=image.img_to_array(img)
# x=np.expand_dims(x, axis=0)
# img_data=preprocess_input(x)
# classes=model.predict(img_data)
# print(classes[0])
# result=int(classes[0][0])
# if result==0:
#     print("Person is Affected By PNEUMONIA")
# else:
#     print("Result is Normal")