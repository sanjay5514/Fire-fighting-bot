import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
import time
from time import sleep
import random
BLYNK_AUTH_TOKEN ="nP8P0xQ7VSmkPnYoQ4M5Sfyk3HGE8M8t"
en1=19
in1=17
in2=18
in3=27
in4=22
en2=21
pp=26
TRIG = 23
ECHO = 24
fl11=5
fl22=6
fl33=13
fl44=25
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.setup(pp, GPIO.OUT)
GPIO.setup(fl11, GPIO.IN)
GPIO.setup(fl22, GPIO.IN)
GPIO.setup(fl33, GPIO.IN)
GPIO.setup(fl44, GPIO.IN)
GPIO.setwarnings(False)
# Set up the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
def p_turn():
    GPIO.output(pp,GPIO.HIGH)
def p_off():
    GPIO.output(pp,GPIO.LOW)
def backward():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(en2,GPIO.HIGH)

    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    
def forward():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(en2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
def stop():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(en2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
def left():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(en2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
def right():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(en2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance
x = 20
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)
def measure_not_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
# Led control through V0 virtual pin
@blynk.on("V0")
def v0_write_handler(value):
#    global led_switch
    if int(value[0]) is not 0:
        forward()
        print('LED1 HIGH')
    else:
        stop()
        print('LED1 LOW')
@blynk.on("V1")
def v1_write_handler(value):
#    global led_switch
    if int(value[0]) is not 0:
        backward()
        print('LED2 HIGH')
    else:
        stop()
        print('LED2 LOW')
@blynk.on("V2")
def v2_write_handler(value):
#    global led_switch
    if int(value[0]) is not 0:
        right()
        print('LED3 HIGH')
    else:
        stop()
        print('LED3 LOW')
@blynk.on("V3")
def v3_write_handler(value):
#    global led_switch
    if int(value[0]) is not 0:
        left()
        print('LED4 HIGH')
    else:
        stop()
        print('LED4 LOW')
@blynk.on("V4")
def v4_write_handler(value):
#    global led_switch
    if int(value[0]) is not 0:
        p_turn()
        measure_not_distance()
        print('LED5 HIGH')
    else:
        p_off()
        print('LED5 LOW')

#function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to New Blynk") 
while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")
        fl1=GPIO.input(fl11)
        fl2=GPIO.input(fl22)
        fl3=GPIO.input(fl33)
        fl4=GPIO.input(fl44)
        if fl4==0:
            stop()
            p_turn()
            sleep(5)
            p_off()
        elif distance < 20:
            stop()
            time.sleep(1)  # Pause for a moment
            
            # Decide randomly to move backward, left, or right
            action = random.choice(['left', 'right'])
            if action == 'backward':
                backward()
                time.sleep(1)  # Move backward for a second
            elif action == 'left':
                left()
                time.sleep(0.5)  # Turn left for a second
            elif action == 'right':
                right()
                time.sleep(0.5)  # Turn right for a second
                RR
            stop()
            time.sleep(0.5)  # Pause for a moment before moving forward again
        elif fl3 == 0:
            forward()
            sleep(0.5)
            stop()
            print('fl3')
        elif fl1 == 0:
            left()
            sleep(0.5)
            stop()
        
            print('fl1')
        elif fl2 == 0:
            right()
            sleep(0.5)
            stop()
            print('fl2')

        else:
            blynk.run()
        time.sleep(0.1)  # Check distance more frequently
