
import RPi.GPIO as gpio
import time


class Drivers():
    def __init__(self):
        
        #Enable forward motor on the drivers
        self.D1_R_EN = 20;
        self.D2_R_EN = 13

        #Enable revers motor on the drivers
        self.D1_L_EN = 21;
        self.D2_L_EN = 6;

        #Forward & Backward for Driver 1
        self.D1_RPWM = 19;
        self.D1_LPWM = 26;

        #Forward & Backward for Driver 2
        self.D2_RPWM = 16;
        self.D2_LPWM = 12;

#       Define all parameters for the drivers
        self.GPIO_PARAMETERS();
        
        self.rpwm_D1 = gpio.PWM(self.D1_RPWM, 100)
        self.rpwm_D2 = gpio.PWM(self.D2_RPWM, 100)

        self.lpwm_D1 = gpio.PWM(self.D1_LPWM, 100)
        self.lpwm_D2 = gpio.PWM(self.D2_LPWM, 100)

        self.rpwm_D1.start(0)
        self.rpwm_D2.start(0)

        self.lpwm_D2.start(0)
        self.lpwm_D1.start(0)        



    def GPIO_PARAMETERS(self):
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        #Set all of our pins to output
        ##############################
        #Enable the DRIVER 1 PINS
        gpio.setup(self.D1_LPWM, gpio.OUT)
        gpio.setup(self.D1_RPWM, gpio.OUT)
        gpio.setup(self.D1_L_EN, gpio.OUT)
        gpio.setup(self.D1_R_EN, gpio.OUT)



        #Enable the DRIVER 2 PINS
        gpio.setup(self.D2_RPWM, gpio.OUT)
        gpio.setup(self.D2_R_EN, gpio.OUT)
        gpio.setup(self.D2_L_EN, gpio.OUT)
        gpio.setup(self.D2_LPWM, gpio.OUT)


        #Enable Left & Right mpvement 

        #DRIVER 1
        gpio.output(self.D1_L_EN, True)
        gpio.output(self.D2_L_EN, True)
        gpio.output(self.D1_R_EN, True)
        gpio.output(self.D2_R_EN, True)





    def Forward(self):
        self.rpwm_D1.ChangeDutyCycle(100)
        self.rpwm_D2.ChangeDutyCycle(75)
        time.sleep(.75);
        self.rpwm_D1.ChangeDutyCycle(0)
        self.rpwm_D2.ChangeDutyCycle(0)
        

    def Backward(self):
        self.lpwm_D1.ChangeDutyCycle(100)
        self.lpwm_D2.ChangeDutyCycle(75)
        time.sleep(.75);
        self.lpwm_D1.ChangeDutyCycle(0)
        self.lpwm_D2.ChangeDutyCycle(0)
