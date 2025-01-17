import cv2 as cv

class Camera:
    def __init__(self):
        self.camera = cv.VideoCapture(1)
        if not self.camera.isOpened():
            raise ValueError("Unable to open camera")
        
        self.camera.set(cv.CAP_PROP_FRAME_WIDTH, 320)
        self.camera.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
        print(f"Camera initialized: width={self.width}, height={self.height}")
        
    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return(ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return(ret, None)
        
        else:
            return None
        

            
