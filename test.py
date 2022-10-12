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

pwm_list = [1400, 1500, 1600, 1500]
dc_list = []
for pwm in pwm_list :
    list.append((pwm*(10**(-6)))/T)

yaw.enable()
pitch.enable()

while(True):
    for dc in dc_list :
      
            #yaw.duty_cycle = pwm/(T*100)
            #pitch.duty_cyle = pwm/(T*100)
        yaw.duty_cycle = dc
        pitch.duty_cycle = dc
        time.sleep(2)
            
    #yaw.duty_cycle = pwm/(T*100)
    #pitch.duty_cycle = pwm/(T*100)
    
