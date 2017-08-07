import RPi.GPIO as io
import time
import cwiid        # Wii Remote library to control the robot
import Motors1      # Includes the functions of the motors as follows:
                            # m1_forward(), m1_backward(), m1_stop()
                            # the same goes for the motors 1 -> 7 

#---------------------------------------------------------
    
button_delay = 0.1          # used for the sleep function between each reading from the wii remote

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)
# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()           
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']          # get the state of the buttons

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)
    
  if (buttons & cwiid.BTN_LEFT):         # if left button is pressed -> motor1 moves forward
    print 'Left pressed'
    m1_forward()
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):         # if right button is pressed -> motor1 moves backwards
    print 'Right pressed'
    m1_backward()
    time.sleep(button_delay)
    
  if (buttons & cwiid.BTN_UP):           # if up button is pressed -> motor2 moves forward
    print 'Up pressed'
    m2_forward()
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_DOWN):         # if down button is pressed -> motor2 moves backwards
    print 'Down pressed'
    m2_backward()
    time.sleep(button_delay)
    
  if (buttons & cwiid.BTN_1):            # if button 1 is pressed -> motor4 moves forward
    print 'Button 1 pressed'
    m4_forward()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):            # if button 2 is pressed -> motor4 moves backwards
    print 'Button 2 pressed'
    m4_backward()
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_PLUS):         # if (+) button is pressed -> motor3 moves forward
    print 'Plus Button pressed'
    m3_forward()
    time.sleep(button_delay)
    
  if (buttons & cwiid.BTN_MINUS):        # if (-) button is pressed -> motor3 moves backwards
    print 'Minus Button pressed'
    m3_backward()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):            # if button A is pressed -> motor5 and motor6 moves forward
    print 'Button A pressed'
    m5_forward()
    m6_forward()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):            # if button B is pressed -> motor5 and motor6 moves backwards
    print 'Button B pressed'
    m5_backward()
    m6_backward()
    time.sleep(button_delay)

  if (not buttons):                     # if there are no buttons pressed -> turn off all motors
    m1_stop()
    m2_stop()
    m3_stop()
    m4_stop()
    m5_stop()
    m6_stop()

  

io.cleanup()
