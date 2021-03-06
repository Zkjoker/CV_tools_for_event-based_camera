import cv2
import numpy as np
def fill_frame(emptyImage,col,row,polarity):
    if(polarity==1):
        emptyImage[col][row] = 0
    else:
        emptyImage[col][row]=255

shape=(180,240)
emptyImage = np.full(shape, 128,dtype='uint8')
timeinteval=0.04
print("已初始化图像矩阵！")
print("准备加载txt文件,文件较大，请耐心等待……")
a=np.loadtxt('insert_data/events.txt')
print("文件加载成功！准备等待生成二值填充图像……")
t=a[:,0:1]  #时间戳
b=a[:,1:3]  #行、列
b=b.astype('uint8')
polar=a[:,3]
polar=polar.astype('uint8')
piccount=1
pointnum=1

for i,j,k in zip(b,t,polar):
    if j<(timeinteval*piccount):
        row=i[0]
        col=i[1]
        #emptyImage[col][row]=0
        fill_frame(emptyImage,col,row,k)
        print("正在填充第{}张图像的第{}个event像素点！".format(piccount,pointnum))
        pointnum=pointnum+1

    else:
        cv2.imwrite("recovery2/{}.jpg".format(piccount),emptyImage)
        print("Program has recovered {} frames!".format(piccount))
        piccount=piccount+1
        pointnum=1
        emptyImage = np.full(shape, 128, dtype='uint8')
        row = i[0]
        col = i[1]
        fill_frame(emptyImage, col, row, k)
        print("正在填充第{}张图像的第{}个event像素点！".format(piccount, pointnum))
        pointnum = pointnum + 1

cv2.imwrite("recovery2/{}.jpg".format(piccount), emptyImage)
print("Program has recovered {} frames!".format(piccount))
print("Finish recovering!")
# cv2.imshow('emptyImage2',emptyImage)
# cv2.waitKey (0)
