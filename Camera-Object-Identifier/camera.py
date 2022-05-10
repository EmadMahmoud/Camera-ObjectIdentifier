import cv2 as cv
import self as self


class Camera:
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        #if there is a problem with the camera we raise an error
        if not self.camera.isOpened():
            raise ValueError("Unable to open the camera")

        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)



        #deconstructor to close the camera when u close the app
    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()


        #getting the next frame
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return(ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret,None)
        else:
            return None
