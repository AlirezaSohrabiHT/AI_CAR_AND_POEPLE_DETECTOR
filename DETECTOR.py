import cv2 
img_file = 'cars.jpg'
classifier_file = 'cars.xml'
img = cv2.imread(img_file)
black_n_white = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
car_tracker = cv2.CascadeClassifier(classifier_file)
cars = car_tracker.detectMultiScale(black_n_white)
print (cars)
cv2.imshow('DETECTOR',black_n_white)
cv2.waitKey()