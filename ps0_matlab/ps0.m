%reading images 1 and 2
img1 = imread('output\ps0-1-a-1.png');
figure, imshow(img1), title('fig 1');

img2 = imread('output\ps0-1-a-2.png');
figure, imshow(img2),title('fig 2');

%part 2 - color planes
%extracting colors form image 1
img1_red = img1(:,:,1); %obtain red pixels
img1_green = img1(:,:,2);%obtain blue pixels
%swap colors from image 1
img1(:,:,1) = img1_green;       %swapping red pixes with blue
img1(:,:,3) = img1_red;
%output the images and save them
figure, imshow(img1),title('color swapped img 1');
imwrite(img1,'output\ps0-2-a-1.png');
figure, imshow(img1_green),title('img 1 - green');
imwrite(img1_green, 'output\ps0-2-b-1.png');
figure, imshow(img1_red),title('img 1 - red');
imwrite(img1_red, 'output\ps0-2-c-1.png');

%part 3 - replacement of pixels
r2 = img2(:,:,1);
g2 = img2(:,:,2);
b2 = img2(:,:,3);
img_better = img1_green(206:306,206:306, :);
figure, imshow(img_better),title('img1-cut out');
img2(206:306,206:306, 2) = img_better;
figure, imshow(img2),title('img2-inserted');
imwrite(img2, 'ps0-3-a-1.png');

%part 4 - Arithmetic and Geometric operations
min_1 = min(min(img1_green));
max_1 = max2(max(img1_green));
mean_1 = mean2(img1_green);
stddev_1 = std2(double(img1_green));

fprintf('min value = %d\n', min_1);
fprintf('max value = %d\n', max_1);
fprintf('mean value = %d\n', mean_1);
fprintf('standard deviation = %d\n', stddev_1);
