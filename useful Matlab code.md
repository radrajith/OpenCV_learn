# Notes and Codes used in Matlab for Computer Vision

#Week 1

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

##Edge Detection

###Sobel operator
![sobel](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/sobel_1.PNG?raw=true)
![sobel-2](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/sobel_2.PNG?raw=true)

```Matlab
%remember to convert the image to double before applying filter
filt = fspecial('sobel');			%filter could be gaussian, sobel, prewitt, roberts: search online for examples
```
##Canny edge operator
```Matlab
edge(image, 'canny');				
```

***
#Week 2

##Hough Transform (finding lines)
We find lines by method of voting
- Each edge points votes for compatible lines
- look for lines that get many votes. 

###Hough Space

The key to hough transform is the hough space. Each point on the image can have a line with mx+b going through it. This is graphed in the hough space, and then a bins are mapped. Which ever bin has the most number of votes, that is most instersecting points in hough space, then that is considered a line. 
![Hough Space](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_1.PNG?raw=true)
![Hough Space2](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_2.PNG?raw=true)

###Polar representation of lines
The hough space for a vertical line will have a slope of infinity, this causes problems. To solve this issue we will deal with polar coordinates.
![Polar representation](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/polar_1.PNG?raw=true)

###Hough Algorithm
![Hough Algorithm](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_algorithm.PNG?raw=true)

```Matlab
%%load image and find the edges using canny operator
edges = edge(image, 'canny');   			%find edges of the image that has been loaded already, using canny operator

%apply hough transform to find candidate lines
[accum theta rho] = hough(edges);			%hough function will return accum - accumulator array, theta - vector of angles, rho - vector of radius values
figure, imagesc(accum, 'XData', theta, 'YData', rho), title('Hough accumulator');

%find peaks in the hough accumulator matrix
peaks = houghpeaks(accum, 100);			%100 - is the maximim number of peaks that we are interested in
hold on; plot(theta(peaks(:,2)), rho(peaks(:,1)), 'rs'); hold off;		%peak return y(radius),x(angle)

%find lines segments
line_segs = houghlines(edges, theta, rho, peaks);

%draw those lines segments on the image
figure, imshow(img), title('Line Segments');
hold on;
for k =1:length(line_segs)
	endpoints = [line_segs(k).point1; line_segs(k).point2];
	plot(endpoints(:,1), endpoints(:,2), 'LineWidth', 2, 'color', 'green');
end
hold off;

%to get better accuracy
%threshold is the minimum value in the accumulator array for  which the peak is recognized. in this case 0.6 times the max accumulator array value
%NHoodSize - region for which the local maxima is computed. [rho, theta] 
peaks = houghpeaks(accum, 100, 'Threshold', ceil(0.6*max(accum(:))),'NHoodSize', [5,5]);
size(peaks)			%this time only 7 peaks are found. 
figure, imagesc(theta, rho, accum), title('Hough Accumulator');
hold on; plot(theta(peaks(:,2)),rho(peaks(:,1)), 'rs'); hold off;

%fillgap is increased to 50 - maximum number of pixels allowed between two segments
%for them to be counted as one, if they lie along the same line 
%To focus more on the longer lines, the minimum lenght is set to be 100 pixels
line_segs = houghlines(edges, theta, rho, peaks, 'FillGap', 50, 'MinLength', 100);	 

%draw those lines segments on the image
figure, imshow(img), title('Line Segments');
hold on;
for k =1:length(line_segs)
	endpoints = [line_segs(k).point1; line_segs(k).point2];
	plot(endpoints(:,1), endpoints(:,2), 'LineWidth', 2, 'color', 'green');
end
hold off;
 	

```

![Hough Demo](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_demo.PNG?raw=true)


###Hough transform for circles(with known radius)
For this case lets assume the radius of the circle is known. the points in the circle will vote in the hough space. The intersection of these varios voting circles will be used as the center point of the circle as described by the image below.
![Hough Cicle](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_circle.PNG?raw=true)

###Hough transform for circles(with unknown radius and without gradient)
In order to find a circle with a unknown radius, though hough transform will have 3 dimentions (a, b, radius), For each points the voting is done in terms of drawing circles in the hough space for various radius(ie creating a cone like structure). By obtaining the intersection the center point can be found. Highly memory intensive process and will find a better algorithm in later classes
![Hough Cicle with unknown radius](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_radius_unknown.PNG?raw=true)

###Hough transform for circles(with unknown radius and with known  gradient)
By obtaining a gradient of a point(slope of the point) the direction of the center of the circle is known. It can be found that the voting for various radius will lie along a line in the hough space(refer to image below). For the intersection of these lines on the hough space the circle be found. 
![Hough Cicle with gradient and unknown radius](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_radius_gradient.PNG?raw=true)

###Hough Algorithm
![Hough Cicle Algorithm](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_circle_algorithm.PNG?raw=true)

###Generalized Hough Transform

building a hough table for an arbitrary object
![Hough table 1](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_table_1.PNG?raw=true)

Finding/Recognizing an object using hough table
![Hough table 2](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/hough_table_2.PNG?raw=true)


###Fourier Transform 

Fourier Properties

![fourier_properties](https://github.com/radrajith/OpenCV_learn/blob/master/notes_images/fourier_properties.PNG?raw=true)

Refer to video of Fourier pair for good examples of how various transforms impacts the image




