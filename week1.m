%%LECTURES NOTES FROM UDACITY - COMPUTER VISION
%% WEEK 1 - 1AL1 - 2AL6
%{

%}
%load image package

brd = imread('test.png');
figure,imshow(brd),title('original');
gray_brd = rgb2gray(brd);
figure, imshow(gray_brd), title('gray');
edge = edge(gray_brd, 'canny',[],2);
figure, imshow(edge), title('edges');

