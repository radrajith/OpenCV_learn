# Notes and Codes used in Matlab for Computer Vision

## Gaussian filter
```Matlab
hsize = 31;			%kernal size
sigma = 5;			%standard deviation of the gaussian distribution
h = fspecial('gaussian', hsize, sigma);		%creating the gaussian filter
surf(h);								%plot the surface graph
outim = imfilter(image, h);	 			%creating a filtered image
imshow(outim);							%output the smoothed image. 
```


![gaussian filter](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/gaussian.PNG?raw=true)
***
## Correlations vs Convolution

![Correlation vs Convolution](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/correlation_convolution.PNG?raw=true)

correlation - essentially the filter is applied exactly. 
covolution - filter is applied after flipping the kernel 180 degrees
***
##Boundary issues

```Matlab
imfilter(f,g,0);			%clip filter, make the boundaries black and then apply filter
imfilter(f,g,'circular') 	%wrap around, fill the right boundaries with the pixel on the left of the image, sort wrapping a paper and making it periodic and then apply filter
imfilter(f,g,'replicate')	%copy edge, fill the boundaries with the pixel on the edge.(extend the pixel on the edge) and then apply filter
imfilter(f,g,'symmetric')	%reflect across edge, make a reflection of the edge for the size of the boundary and then apply the filter
```
***
## Noise
```Matlab
imnoise(img, 'salt&pepper', 0.02);			%create salt&pepper noise on the image
```

***
##Median filter
```Matlab
median filter = medfilt2(noisy_img);		%median filter in two dimension
```
***
##Normalized correlation (using filter as template matching)
###1D normalized correlation
1D normalized correlation. As seen from image below, the peak of the normalized function is at the location where the filter is same as the original signal
![1D normalized Correlation](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/normalized_correlation_1.PNG?raw=true)

###2D normalized correlation
The filter is cropped from the peppers image. When the normalized correlation is applied and plotted, the peak is said to be the exact match of the filter. 
![2D normalized Correlation-1](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/normalized_correlation_2.PNG?raw=true)

![2D normalized Correlation-2](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/normalized_correlation_3.PNG?raw=true)

###Matlab code for finding the template in 1D signal
```Matlab
pkg load image;		%load image package

function index = find_template_1d(t,s)
	c = normxcorr2(t,s);			%normalized correlation function to compare and return the output with peaks
	[maxValue rawIndex] = max(c); 	%find the peak values from the returned correlation
	index = rawIndex = size(t,2) +1; %since the rawIndex value is the end point we have to subract the size of the filter from it 
end function

s=[-1 0 0 1 1 1 0 -1 -1 0 1 0 0 1]
t=[ 1 1 1]
disp('signal:'), disp([1:size(s,2); s]);
disp('tempalte:'), disp([1:size(t,2); t]);

index = find_template_1d(t,s);
disp('Index:'), disp(index);
```
###2D matlab code and result
![2D normalized -Matlab code](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/normalized_correlation_4.PNG?raw=true)

![2D normalized -Result](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/normalized_correlation_5.PNG?raw=true)

***




