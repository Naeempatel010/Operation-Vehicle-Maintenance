import os
import cv2

video_name = 'video6.avi'

image_folder = r"normalvideo"
mask_folder = r"maskedvideo"

imgsortlist1 = os.listdir(image_folder)	
print('imgsortlist', imgsortlist1)

masked_images = os.listdir(mask_folder)

img_sort = zip(imgsortlist1, [int(i.split('.')[0]) for i in imgsortlist1 if i.endswith(".jpg")])
img_sort = sorted(img_sort, key = lambda x: x[1])
print('img_sort', img_sort)
img_sort_fin = list(zip(*img_sort))
print('img_sort_fin', img_sort_fin)
img_sort_final = img_sort_fin[0]
#print(img_sort_final)
images = [img for img in img_sort_final if img.endswith(".jpg")]
print('images', images)

frame = cv2.imread(os.path.join(image_folder, masked_images[0]))
height, width, layers = frame.shape
print(height)
print(width)

video = cv2.VideoWriter(video_name, 0, 30, (width,height))

for image in images:
	img=cv2.imread(os.path.join(image_folder, image))
	if img is not None:

		resized= cv2.resize(img, (width,height))
		print(resized)
		video.write(resized)

cv2.destroyAllWindows()
video.release()