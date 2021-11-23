import cv2
from cv2 import namedWindow
from sensor_msgs.msg import Image
import rospy
from cv_bridge import CvBridge

class opencv_test:
    def __init__(self):
        rospy.init_node('image_converter')
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/thorvald_001/kinect2_front_camera/hd/image_color_rect", Image, self.image_callback,queue_size=1)
        self.image_pub = rospy.Publisher("thorvald_001/kinect2_front_camera/hd/image_modified", Image, queue_size=1)

    def image_callback(self, image):
        print("received image")
        namedWindow("Modified images")

        cv_image = self.bridge.imgmsg_to_cv2(image)
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(1)

#startWindowThread()
if __name__ == "__main__": 
    opencv_test()
    rospy.spin()
#destroyAllWindows()