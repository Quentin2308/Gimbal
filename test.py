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

pwm_list = [1300, 1500, 1600]
list = [0.4, 0.5, 0.6]
yaw.enable()
pitch.enable()
try :
    while(True):
        for i in list :
      
            #yaw.duty_cycle = pwm/(T*100)
            #pitch.duty_cyle = pwm/(T*100)
            yaw.duty_cycle = i
            pitch.duty_cycle = i
            time.sleep(2)
            
    #yaw.duty_cycle = pwm/(T*100)
    #pitch.duty_cycle = pwm/(T*100)
    
except KeyboardInterrupt :
    yaw.close()
    pitch.close()
    print ("interruption par l'utilisateur")
