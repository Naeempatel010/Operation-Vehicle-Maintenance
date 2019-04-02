# Program To Read video 
# and Extract Frames 
import cv2 
from evaluate import predict_mask,checkmask
import os

image_folder = r"normalvideo"

# Function to extract frames 
def FrameCapture(path): 
	
	# Path to video file 
	vidObj = cv2.VideoCapture(path) 

	# Used as counter variable 
	count = 0

	# checks whether frames were extracted 
	success = 1

	while success: 

		# vidObj object calls read 
		# function extract frames 
		success, image = vidObj.read() 

		# Saves the frames with frame-count 
		cv2.imwrite("normalvideo/%d.jpg" % count, image) 

		count += 1
		count


# Driver Code 
if __name__ == '__main__': 

	# Calling the function 
	FrameCapture(r"videos/vid.mp4") 


step = 10
start=15

len_imgs  = len(os.listdir(image_folder))
no_of_frames=len_imgs/step

#list_out = [str(i)+'.jpg' for i in range(start, len_imgs, step) ]
# for i in range(start, count, step):
# 	print(i)
# 	list_out = list_out.append(i +'.jpg')

#print(list_out)

list_out_new=[]
list_out=[]
i=start
count=0
while i<len_imgs:
	if count>25:
		break
	print(i)
	flag=checkmask("normalvideo/"+str(i)+".jpg","maskedvideo/"+str(i)+".jpg")
	if flag==1:
		list_out_new.append("normalvideo/"+str(i))
		step_size=5
		count=count+1

	else:
		step_size=10
	i=i+step_size

print(list_out_new)



