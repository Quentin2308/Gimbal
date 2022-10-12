import time
from periphery import GPIO

from periphery import PWM
    
#frequency and period
f = 50
T = 1/f
   
SERVO_MIN_VAL = 500
SERVO_MAX_VAL = 2500
    
YAW_PIN = 11
PITCH_PIN = 13
  
yaw = PWM(0, 0)
pitch = PWM(0, 1)

yaw.frequency = f
pitch.frequency = f

#pwm = 
list = [0.2, 0.8]
try :
    while(True):
        for i in list:
            yaw.enable()
            pitch.enable()
            yaw.duty_cycle = i
            pitch.duty_cyle = i
            time.sleep(0.5)
            yaw.disable()
            pitch.disable()
    #yaw.duty_cycle = pwm/(T*100)
    #pitch.duty_cycle = pwm/(T*100)
    
except KeyboardInterrupt :
    yaw.close()
    pitch.close()
    print ("interruption par l'utilisateur")
