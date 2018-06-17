import RPi.GPIO as GPIO
import time
control = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5]

control1 =[12.5,12,11.5,11,10.5,10,9.5,9,8.5,8,7.5,7,6.5,6,5.5,5,4.5,4,3.5,3,2.52,1.5,1,0.5,0] 
servo = 22

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo,GPIO.OUT)
# in servo motor,
  # 1ms pulse for 0 degree (LEFT
  # 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

p=GPIO.PWM(servo,100)# 50hz frequancy

p.start(0)# starting duty cycle ( it set the servo to 0 degree )

t = 0.25
try:
    for x in control:
        p.ChangeDutyCycle(x)
        time.sleep(t)

    for x in control1:
        p.ChangeDutyCycle(x)
        time.sleep(t)

except KeyboardInterrupt:
        GPIO.cleanup()
