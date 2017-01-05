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

## Correlations vs Convolution

![Correlation vs Convolution](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/correlation_convolution.PNG?raw=true)

correlation - essentially the filter is applied exactly. 
covolution - filter is applied after flipping the kernel 180 degrees

##Boundary issues

```Matlab
imfilter(f,g,0);			%clip filter, make the boundaries black and then apply filter
imfilter(f,g,'circular') 	%wrap around, fill the right boundaries with the pixel on the left of the image, sort wrapping a paper and making it periodic and then apply filter
imfilter(f,g,'replicate')	%copy edge, fill the boundaries with the pixel on the edge.(extend the pixel on the edge) and then apply filter
imfilter(f,g,'symmetric')	%reflect across edge, make a reflection of the edge for the size of the boundary and then apply the filter
```

