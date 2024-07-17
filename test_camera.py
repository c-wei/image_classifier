import cv2 as cv

def test_camera():
    camera = cv.VideoCapture(1)
    if not camera.isOpened():
        print("Error: Unable to open camera")
        return
    
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Unable to capture frame")
            break
        
        cv.imshow('Camera Test', frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    camera.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    test_camera()