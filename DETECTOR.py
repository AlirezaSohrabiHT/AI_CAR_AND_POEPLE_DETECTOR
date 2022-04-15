import cv2 
img_file = 'cars.jpg'
video = cv2.VideoCapture('cars.mp4')
classifier_file = 'cars.xml'
car_tracker = cv2.CascadeClassifier(classifier_file)
while True:
 (read_successful, frame)=video.read() 
 if read_successful:
      grayscaled_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 else: 
      break

 cars = car_tracker.detectMultiScale(grayscaled_frame)
 print(cars)
 cv2.imshow('DETECTOR',grayscaled_frame)
 cv2.waitKey(1)

#img = cv2.imread(img_file)
#black_n_white = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
#for(x,y,w,h) in cars:
#cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#print (cars)
