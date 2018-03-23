import sys
import time
import RPi.GPIO as GPIO

redLed = 21
freq = int(sys.argv[2])
GPIO.setmode(GPIO.BCM)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(redLed, GPIO.LOW)
ledOn = False



print("\n [INFO] Blinking LED (5 times) connected at GPIO {0} at every {1} second(s)".format(redLed, freq))
for i in range(5):
    GPIO.output(redLed, GPIO.LOW)
    time.sleep(freq)
    GPIO.output(redLed, GPIO.HIGH)
    time.sleep(freq)

# do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff \n")
GPIO.cleanup()
