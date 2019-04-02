from keras.models import load_model
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.layers import Dense, Activation, Flatten, Dropout
from keras.models import Sequential, Model
import numpy as np
HEIGHT = 150
WIDTH = 150
model_weights_path="checkpoints/new_model_weights.h5"
model=VGG16(weights='imagenet',include_top=False,input_shape=(HEIGHT, WIDTH, 3))
x=model.output
dropout=0.5
num_classes=4
fc_layers = [1024, 1024]
x= Flatten()(x)
for fc in fc_layers:
	x = Dense(fc, activation='relu')(x) 
	x = Dropout(dropout)(x)
	predictions = Dense(num_classes, activation='softmax')(x) 
	model= Model(inputs=model.input, outputs=predictions)

model.load_weights(model_weights_path)

img_width=150
img_height=150
def predict(file,bodypart):
	x = load_img(file, target_size=(img_width,img_height))
	x = img_to_array(x)  
	x = np.expand_dims(x, axis=0)
	array = model.predict(x)
	answer = np.argmax(array)
	class_list = ["Trunk", "Side View", "Bonnet","Wheels"]
	a=class_list[answer]
	print("a is"+a)	
	if a==bodypart:
		return "yes"
	else:
		return "no"