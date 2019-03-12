import cv2
vc = cv2.VideoCapture('avi_file/Denosed_event_slow(6010).avi')  # 读入视频文件
if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
    print("Success open!")
else:
    rval = False

count = 1 #记帧
timeF = 1  # 视频帧计数间隔频率
filecount=0
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (count % timeF == 0):  # 每隔timeF帧进行存储操作
        filecount=filecount+1
        filename='frame/6010/'+str(filecount)+'.jpg'
        cv2.imwrite(filename, frame)  # 存储为图像
        print("Now is generating {} picture".format(filecount))
    cv2.waitKey(1)##切换到下一帧图像
vc.release()
