% ps1

%% 1-a
img = imread(fullfile('input', 'ps1-input0.png'));  % already grayscale
figure, imshow(img), title('Original Image');
%% TODO: Compute edge image img_edges
img_edges = edge(img, 'canny'); 
% since its a binary image the threshold will have no impact
figure, imshow(img_edges), title('img1a - edges');
imwrite(img_edges, fullfile('output', 'ps1-1-a-1.png'));  % save as output/ps1-1-a-1.png

%% 2-a
[H, theta, rho] = hough_lines_acc(img_edges);  % defined in hough_lines_acc.m
%% TODO: Plot/show accumulator array H, save as output/ps1-2-a-1.png
figure, imagesc(H), title('2a - accumulator array');
imwrite(H, fullfile('output', 'ps1-2-a-1.png'));
%Checking if my hough and build in hough matches
%[H, theta, rho] = hough(img_edges);  % defined in hough_lines_acc.m
%figure, imagesc(H), title('2atest - accumulator array');


%% 2-b
%peaks = hough_peaks(H, 10);  % defined in hough_peaks.m
%% TODO: Highlight peak locations on accumulator array, save as output/ps1-2-b-1.png
peaks = houghpeaks(H,10);
figure, plot(theta(peaks(:,2)),rho(peaks(:,1)),'rs'), title('2b - peaks');
imwrite(peaks, fullfile('output', 'ps1-2-b-1.png'));
%% TODO: Rest of your code here


%}