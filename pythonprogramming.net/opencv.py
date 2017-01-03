import cv2
import numpy as np
from matplotlib import pyplot as plt

#############vid 1##################
# img = cv2.imread('cake.jpg', cv2.IMREAD_GRAYSCALE)      #import and convert to grayscale
# cv2.imshow('image', img)                                #
# cv2.waitKey(0)                                          #wait for key to press
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')   #displaying using matplotlib
# plt.plot([50,100],[80,100],'c',linewidth=5)             #drawing on the image
# plt.show()

# cv2.imwrite('savepic.png',img)                              #to save an image


###############vid 2#######################

# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')                    #to write to a file, set the codec we want to use
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480)) #size is 640x480
# while True:
#     ret, frame = cap.read()                                 #ret = true or false if there is a feed; frame gets the video feed
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          #conver the color of the frame to gray
#     out.write(frame)                                        #write the current frame to the output file
#     cv2.imshow('frame', frame)
#     cv2.imshow('gray',gray)
#
#     if  cv2.waitKey(1) & 0xff == ord('q'):                   #if q is presssed during the infinite loop, exit the loop
#         break
# cap.release()                                               #release the camera
# out.release()
# cv2.destroyAllWindows()

#############vid 3 ###############################
# img = cv2.imread('cake.jpg', cv2.IMREAD_COLOR)
# cv2.line(img,(0,0),(150,150), (255,255,255),15)                       #drawing a line on the image, Remember its BGR not RGB
# cv2.rectangle(img,(15,25), (200,150),(255,0,0), 5)
# cv2.circle(img,(150,33), 23, (0,255,0), -1)                             #-1 fill the circle
# #for drawing polygon, first we declare the points and later connect them
# pts = np.array([[10,5],[20,12],[70,30],[50,10]], np.int32)                #array of numbers, with the data type of int32
# pts = pts.reshape((-1,1,2))                                             #reshape the array to be 1 x 2
# cv2.polylines(img, [pts], True, (0,255,255), 3)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, 'helloworld',(100,100),font,1,(123,123,132),3)
#
#
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##########vid 4#####################################
# img = cv2.imread('cake.jpg',cv2.IMREAD_COLOR)
# px = img[55,55]                                                     #obtain the specific pixel color
# img[100,100] = [255,255,255]
# cv2.imshow('image',img)
# #ROI - region of image
# roi = img[100:150, 100:150]                                         #print the values at that region
# print(roi)
#
# img[100:150, 100:150] = [255,255,255]
# cv2.imshow('imgmod',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#########vid 5####################################
#
# img1 = cv2.imread('img1.png')
# img2 = cv2.imread('img3.png')
#
# #add = img1 + img2                                                  #overlapping both images
# # add = cv2.add(img1,img2)
# #weighted = cv2.addWeighted(img1, .6, img2, .4, 0)                  #adding based on weights alotted to the images
#
# rows,cols,channels = img2.shape                                     #obtain the dimesntions of the image
# roi = img1[0:rows, 0:cols]                                          #select the region of the image
# img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)  #any pixel that is over 220 will be defaulted to 255 = white, if below 220, then 0 = blue and then invert that
# mask_inv = cv2.bitwise_not(mask)                                        #invert the colors
# img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)                      #take the img1 mask the inverted image 2 with it(make the img1 as the background of img2)
# img2_fg = cv2.bitwise_and(img2,img2,mask = mask)                        #take the img2, mask with the black and white logo(mask), so that 'and' will make only the white part remain -(obtain the logo without the background)
# dst = cv2.add(img1_bg, img2_fg)                                         #add the both post process images, the black is 0, so all the black from img1 will be filled with the color from img2, making it look like having different background
# img1[0:rows, 0:cols] =dst                                               #paste the processed/modified image(dst) on top of the img1
# cv2.imshow('res',img1)
# cv2.imshow('img1_bg',img1_bg)
# cv2.imshow('img2_fg',img2_fg)
# cv2.imshow('dst',dst)
# cv2.imshow('image_add', mask)
# cv2.imshow('img_inv', mask_inv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

###########vid 6#########################################
# img1 = cv2.imread('bookpage.jpg')
#
# ret, thres = cv2.threshold(img1,12,255,cv2.THRESH_BINARY)
#
# r,c,ch = img1.shape
# roi = img1[0:r, 0:c]
#
# #img2 = cv2.bitwise_and(roi,roi)
# img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# ret, thres2= cv2.threshold(img2,12,255,cv2.THRESH_BINARY)
#
# gaus = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51,1)
#
# cv2.imshow('img1',img2)
# cv2.imshow('thres',thres)
# cv2.imshow('gaus',gaus)
# cv2.imshow('thres2',thres2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#######vid 7##############################################
# cap = cv2.VideoCapture(0)
# while True:
#     _, frame = cap.read()           # _ is used to obtain the values, but is ignored since its not necessary
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     #hsv hue sat value
#     low_blk = np.array([100,0,0])
#     up_blk = np.array([150,255,255])
#
#     mask = cv2.inRange(hsv,low_blk,up_blk)
#     res = cv2.bitwise_and(frame,frame, mask = mask)
#     cv2.imshow('frame', hsv)
#     cv2.imshow('mask', mask)
#     cv2.imshow('res', res)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

############vid 8############################################

# cap = cv2.VideoCapture(0)
# while True:
#     _, frame = cap.read()           # _ is used to obtain the values, but is ignored since its not necessary
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     #hsv hue sat value
#     low_blk = np.array([50,0,0])
#     up_blk = np.array([70,255,255])
#
#     mask = cv2.inRange(hsv,low_blk,up_blk)
#     res = cv2.bitwise_and(frame,frame, mask = mask)
#
#     ##averaging
#     kernel = np.ones((15,15),np.float32)/255
#     smoothed = cv2.filter2D(res, -1, kernel)
#
#     ##gaussian blur
#     blur = cv2.GaussianBlur(res, (15,15),0)
#     ##median blur
#     median = cv2.medianBlur(res, 15)
#     ##bilateral blur
#     bilateral = cv2.bilateralFilter(res, 15, 75, 75)
#
#     cv2.imshow('frame', hsv)
#     cv2.imshow('mask', mask)
#     cv2.imshow('res', res)
#     cv2.imshow('smoothed', smoothed)
#     cv2.imshow('blur', blur)
#     cv2.imshow('median', median)
#     cv2.imshow('bilateral', bilateral)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

#######vid 9###################################################
#
# cap = cv2.VideoCapture(0)
# while True:
#     _, frame = cap.read()           # _ is used to obtain the values, but is ignored since its not necessary
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     #hsv hue sat value
#     low_blk = np.array([50,0,0])
#     up_blk = np.array([70,255,255])
#
#     mask = cv2.inRange(hsv,low_blk,up_blk)
#     res = cv2.bitwise_and(frame,frame, mask = mask)
#
#     kernel = np.ones((5,5), np.uint8)
#     erosion = cv2.erode(mask, kernel, iterations=1)
#     dilation = cv2.dilate(mask, kernel, iterations=1)
#     openning = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)                   #removes false positives in the noise
#     closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)                   #removes false negatives in the noise
#
#     cv2.imshow('frame', hsv)
#     cv2.imshow('mask', mask)
#     cv2.imshow('res', res)
#     cv2.imshow('erosion', erosion)
#     cv2.imshow('dilation', dilation)
#     cv2.imshow('openning', openning)
#     cv2.imshow('closing', closing)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

###########vid 10 #################################################
#
# cap = cv2.VideoCapture(0)
# while True:
#     _, frame = cap.read()           # _ is used to obtain the values, but is ignored since its not necessary
#     # gradient
#     laplacian = cv2.Laplacian(frame, cv2.CV_64F)
#     sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize= 5)
#     sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
#     # edge detection
#     edges = cv2.Canny(frame, 100, 100)
#
#     cv2.imshow('img', frame)
#     cv2.imshow('laplace', laplacian)
#     cv2.imshow('sobelx', sobelx)
#     cv2.imshow('sobely', sobely)
#     cv2.imshow('edges', edges)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

###############vid 11 ###################################################
# img_bgr = cv2.imread('template.jpg')
# img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
#
# template = cv2.imread('template2.jpg',0)
# w, h = template.shape[::-1]
#
# res = cv2.matchTemplate(img_gray,template, cv2.TM_CCOEFF_NORMED)
# threshold = 0.75
# loc = np.where(res>=threshold)
#
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255),2)
#
# cv2.imshow('detected', img_bgr)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

###############vid 12############################################
# img = cv2.imread('img1.jpg')
# mask = np.zeros(img.shape[:2], np.uint8)
#
# bgmodel = np.zeros((1,65), np.float64)
# fgmodel = np.zeros((1,65), np.float64)
#
# rect = (161,79, 150, 150)
# cv2.grabCut(img, mask, rect, bgmodel, fgmodel, 5, cv2.GC_INIT_WITH_RECT)
# mask2 = np.where((mask ==2)|(mask==0), 0,1).astype('uint8')
# img = img*mask2[:,:,np.newaxis]
# plt.imshow(img)
# plt.colorbar()
# plt.show()

####################################
nums = [3,2,4]
target = 6
for i in range(0, len(nums) - 1):
    for j in range(i+1, len(nums)):
        if (nums[i] + nums[j] == target):
            print [i, j]