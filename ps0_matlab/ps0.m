img1 = imread('output\ps0-1-a-1.png');
imshow(img1);
%pause;
img2 = imread('output\ps0-1-a-2.png');
imshow(img2);
%pause;
size(img1);
size(img2)
img1_red = img1(:,:,1);
img1_green = img1(:,:,2);
img1(:,:,1) = b1;       %swapping red pixes with blue
img1(:,:,3) = img1_red;
imshow(img1);
pause;
imshow(img1_red);
pause;
imshow(img1_green);
imwrite(img1, 'output\ps0-2-b-1.png');      %writing to file.
imwrite(img1_green, 'output\ps0-2-b-1.png');
imwrite(img1_red , 'output\ps0-2-c-1.png');
r2 = img2(:,:,1);
g2 = img2(:,:,2);
b2 = img2(:,:,3);
-
