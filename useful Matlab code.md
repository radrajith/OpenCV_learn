# Codes used in Matlab for Computer Vision

### Gaussian filter
```Matlab
hsize = 31;			#kernal size
sigma = 5;			#standard deviation of the gaussian distribution
h = fspecial('gaussian', hsize, sigma);		#creating the gaussian filter
surf(h);								#plot the surface graph
outim = imfilter(image, h);	 			#creating a filtered image
imshow(outim);							#output the smoothed image. 
```


![gaussian filter](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/gaussian.PNG?raw=true)
