### Operational Vehicle Maintenance using AR/VR Developed for the Smart India Hackathon 2019, The world's Largest Hackathon with nearly 784 Teams for across the country Participating.

This project won the First Prize at the Hackathon.This project was modified to make it suitable to work for the Operational vehicle maintainance. we use the base model of Matterport Masked RCNN for which I express my gratitude for making it open source https://github.com/matterport/Mask_RCNN

## Steps :-

# 1. Annotating the Data

A Mask R-CNN model requires the user to annotate the images and identify the region of damage. The annotation tool I used is the VGG Image Annotator — v 1.0.6. You can use the html version available at http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html . Using this tool you can create a polygon mask as shown below:

![annotating images](https://github.com/Naeempatel010/Operation-Vehicle-Maintenance/blob/master/results/a.jpg)

Once you have created all the annotations, you can download the annotation and save it in a json format. You can look at my images and annotations on my repository here.


# 4. Training

After the Data Collection and annotation part, we move onto the training aspect of the Mask-RCNN. Without going into the details of how the training takes place, I have provided a simple python command in order to do the training. Please utilize a GPU if you don't want to wait till Eternity!!

there are three ways you can train the model

1. From scratch 

``` bash

foo@bar :~$ python3 custom.py train --dataset=/path/to/datasetfolder 

```
2. Transfer Learning using COCO weights as the starting point( This is highly recommended for use!)
``` bash
foo@bar :~$ python3 custom.py train --dataset=/path/to/datasetfolder --weights=coco

```
3. Resuming a previous Training
```bash 
foo@bar :~$ python3 custom.py train --dataset=/path/to/datasetfolder --weights=last

```


# 5. Testing and Inference 

For this specific purpose, I have an entire Directory dedicated to provide many functionalities. These are :- 

1. To run a tornado server, ```server3.py``` 
2. to run the inference without the server using command line ```evaluate.py```
3.  A utility module to import and use the mask R-CNN  ```predicfunc.py```

Along with this , there are few Jupyter files provided in the source by Matterport in order to better understand how the entire inference works. Also note that mask R-CNN without the gpu take a very long time. For our model it took nearly 18 seconds to make a prediction!!

## 6. Screenshots 

# Before

![before](https://github.com/Naeempatel010/Operation-Vehicle-Maintenance/blob/master/results/image78.jpg)


# After
![after](https://github.com/Naeempatel010/Operation-Vehicle-Maintenance/blob/master/results/image78_masked.jpg)


# Before
![before](https://github.com/Naeempatel010/Operation-Vehicle-Maintenance/blob/master/results/image80.jpg)


# After
![output](https://github.com/Naeempatel010/Operation-Vehicle-Maintenance/blob/master/results/image80_masked.jpg)
