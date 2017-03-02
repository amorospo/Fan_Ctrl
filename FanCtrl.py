#!/usr/bin/python

#Simple FAN control with transistor for Raspberry Pi 3
#Author: Stefano Novelli
#Email: murdercode@gmail.com
#Website: www.inforge.net

####### Modified by amorospo #######
######### amorospo@yahoo.it ########

#Import libraries
import RPi.GPIO as GPIO #importo i moduli di GPIO
import time, subprocess, string #importo altri moduli utili

############### CHOOSE YOUR PERSONAL SETTINGS!!! ###############
fanPin = 21 #definisco la porta GPIO che usero' per attivare il transistor
maxTemp = 50 #definisco la temperatura massima
delta = 5 #definisco di quanti gradi voglio abbassare la temperatura prima di spegnere la ventola

GPIO.setmode(GPIO.BCM) #imposto la lettura dello schema della GPIO a BCM
GPIO.setwarnings(False) #disabilito i messaggi di stato
GPIO.setup(fanPin, GPIO.OUT) #dico al pin della ventola che deve lavorare in output

while True: #eseguo un ciclo infinito

        out = subprocess.check_output(['/opt/vc/bin/vcgencmd','measure_temp']) #ottengo la CPU temp dal tool unix
        outx = string.split(out, '=') #esplodo il risultato in un array
        outy = string.split(outx[1], "'") #esplodo il risultato in secondo array
        temp = float(outy[0]) #converto il valore da stringa a float

        if temp > maxTemp: #se la temperatura e' raggiunta
                GPIO.output(fanPin, 1) #chiudo il circuito attivando il transistor
        elif temp < maxTemp - delta: #se la temperatura si e' abbassata a sufficienza
                GPIO.output(fanPin, 0) #riapro il circuito disattivando il transistor

        time.sleep(15) #attendo 15 secondi
