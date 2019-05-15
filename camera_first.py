from picamera import PiCamera

from time import sleep

camera = PiCamera()

#transparency of camera screen (from 0 --> transparent to 255 --> opaque)
camera.start_preview(#alpha=200)
#to take video
camera.start_recording('/home/pi/Desktop/TestingBelt2.h264')

#the time camera will run for.

sleep(30)

#to take picture.
#camera.capture('/home/pi/Desktop/image.jpg')

#camera.rotation
#camera.rotation=180 #value can be 90,180,270,0


camera.stop_recording()
camera.stop_preview()
  
#when playing video use: 
  #omxplayer /home/pi/Desktop/TestingBelt2.h264(from the top)
  


