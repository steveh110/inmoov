def trackHumans():
  i01.headTracking.faceDetect()
  i01.eyesTracking.faceDetect()
  i01.setHeadVelocity(80, -1)
  sleep(1)
  fullspeed()

