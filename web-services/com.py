import cv2
import os
from shutil import copyfile


image_folder = r"normalvideo"
mask_folder = r"maskedvideo"

video_name = 'video1.avi'
imgsortlist = os.listdir(image_folder)










masked_images = os.listdir(mask_folder)

rep_count  = 1
rep_list = [[ str(m)+'.jpg' for m in range(int(mi.split('.')[0]) - rep_count, int(mi.split('.')[0]) + rep_count)   ] for  mi in masked_images] 

rep_list = sum(rep_list, [])

#print('rep_list', rep_list)
# for rep in rep_list:
# 	os.remove(rep)
imgsortlist = os.listdir(image_folder)	
print(masked_images)

for rep in masked_images:
	for img_name in range(int(rep.split('.')[0]) - rep_count, int(rep.split('.')[0]) + rep_count):
		copyfile(mask_folder+ '/' + rep, image_folder + '/' + str(img_name) +'.jpg')

