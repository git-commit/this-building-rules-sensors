import RPi.GPIO as GPIO
import time

import requests

window_id = "a2394935-749c-4783-b159-097a83a5a32b" 
url = "https://api.preview.oltd.de/v1/devices/"

endpoint = url + window_id  
token = {"Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJNRWo4QkVEaWZnSnBfTzB3OEJCbEYxU05TNElmdlMyLWhERFBWTDRaTDYwIn0.eyJqdGkiOiJlNjU2M2Y4ZS1lMzc0LTRkZWEtODFkMy05NjQwYTVlNWIxZWYiLCJleHAiOjE1Mjk5NDc2NzEsIm5iZiI6MCwiaWF0IjoxNTI5MDk2OTYyLCJpc3MiOiJodHRwczovL2FwaS5wcmV2aWV3Lm9sdGQuZGUvYXV0aC9yZWFsbXMvb2x0IiwiYXVkIjoib2x0X3BvcnRhbCIsInN1YiI6ImIwNzc1Yjc0LWExYjAtNDAzOS1hMzcxLTg4N2Y1ZjIxZTJmYyIsInR5cCI6IkJlYXJlciIsImF6cCI6Im9sdF9wb3J0YWwiLCJub25jZSI6IlVIeElWVkdET1ZzbjhZbkdEU1o1QWdlTWl5YW1PQUFrVE83SjFqU3UiLCJhdXRoX3RpbWUiOjE1MjkwODM2NzEsInNlc3Npb25fc3RhdGUiOiJmZTFlYWJiMC1mMGVhLTQ5ZjEtYTNjNC1jODZhMThjNGIyNGEiLCJhY3IiOiIwIiwiYWxsb3dlZC1vcmlnaW5zIjpbXSwicmVzb3VyY2VfYWNjZXNzIjp7fSwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6ImJlcmdlci5tYXhpbWlsaWFuQGdteC5kZSIsImdpdmVuX25hbWUiOiJNYXhpbWlsaWFuIiwiZmFtaWx5X25hbWUiOiJCZXJnZXIiLCJlbWFpbCI6ImJlcmdlci5tYXhpbWlsaWFuQGdteC5kZSIsInRlbmFudCI6IjgwNWM0NDIwLTQxNjEtNGI0ZC1iZDI4LTNkMzNmNjkxZjI0MSJ9.jJqDQ4Y2srcJjUMY98F7u4EXVhBlTInLND6UFs5b1cF6iUczMedn_bK-hcNIzPnBAtEO8330vZ4pnYED5Kr5Whuwl6Z1_hVfa7d_zQ2I01prCpPZX7syQZqX-fvPqUDjpXITPUyAli03Eo6VVhZVI7HpHj5sh1qEa4Xr2qitRXAHqUgC5jw8WOPOL7Mwpmy9UmoKZVdTOrhYsuM1tIeShkQNOjBy2iYbi7OBHn2Gl74zPwqcqnL1jUgYeLjsYNKbTB-VB2VUtzIJXC_jeYraJLNWoqBQpgBUgr-YgkeXgG2kB9PmEHeXW2f6AeLtf3uHSLMqnFixK2SAhtej3-DQGA"}

r = requests.get(endpoint, headers=token)
print(r.json())
old_state = r.json()['data']['custom']['open'] 

while(True):
    r = requests.get(endpoint, token)
    state = r.json()['data']['custom']['open']
    if state != old_state:
        if state:
            print("close window")
        else:
            print("open window")
        print("changed state to" + str(state))
    time.sleep(1)



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
