import math,cv2,numpy as np,matplotlib.pylab as plt,time

def masked_roi(image,vertices_roi):
	mask=np.zeros_like(image)
	cv2.fillPoly(mask, vertices_roi,255) #takes all the color_channels
	return cv2.bitwise_and(image, mask)

def draw_lines(image,lines):
	img=np.copy(image)
	line_img=np.zeros(img.shape,dtype=np.uint8)
	try:
		for line in lines:
				for x1,y1,x2,y2 in line:
					cv2.line(line_img,(x1,y1),(x2,y2),(0,255,0),10) 
				#pass the empty img and mask with it
	except:
		pass
	img=cv2.addWeighted(img,0.8,line_img,1.0,0.0)
	return img


def detect_lanes(img):

	#path= r"D:/Cyberpunkk OpenCV/Lane Detection/test_image.png"
	#img=cv2.imread(path)
	#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	h=img.shape[0]
	w=img.shape[1]
	print(h,w)
	vertices_roi= [(200,710),(650,557),(900,710)]
	gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	#cv2.imshow('gray',gray)
	canny=cv2.Canny(gray,100,120)
	crop_img=masked_roi(canny,np.array([vertices_roi],np.int32))
	#cv2.imshow('crop_img',crop_img)

	lines=cv2.HoughLinesP(crop_img,rho=6,theta=np.pi/180,threshold=100,lines=np.array([]),minLineLength=100,maxLineGap=30)
	if lines is None:
		img_lines=img
	img_lines=draw_lines(img,lines)
	return img_lines
	'''
	plt.imshow(img_lines)
	plt.show()'''


cap=cv2.VideoCapture('D:\lanes3.mp4')


while (cap.isOpened()):
	
	_,frame=cap.read()
	#plt.imshow(frame)  use this plot to edit vertices_roi to form a triangle which cover the current lane
	#plt.show()
	frame=detect_lanes(frame)
	cv2.imshow('vide',frame)
	
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()