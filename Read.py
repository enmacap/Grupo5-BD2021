#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import simpleMFRC522

obj = SimpleMFRC522()

try:
        leer = input('Nuevo Personal:')
        print("Ponga su tarjeta para registrarse")
        obj.write(leer)
        print("Tarjeta leida")
finally:
        GPIO.cleanup()
        
try: 
        id, leer= obj.read()
        print(id)
        print(leer)
finally:
        GPIO.cleanup()
        
