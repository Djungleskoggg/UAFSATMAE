import cv2
print(f"OpenCV Version: {cv2.__version__}")

#0 for usb camera
camera_index = 0 

cam = cv2.VideoCapture(camera_index)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame. Is the camera disconnected?")
        break
        
    cv2.imshow('USBCam', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()