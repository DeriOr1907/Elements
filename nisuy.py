import pywhatkit
import time
from datetime import datetime
import pygame
def send_sms(msg,ph):
    t = time.localtime()
    current_h = int(time.strftime("%H", t))
    current_m = int(time.strftime("%M", t)) % 60
    pywhatkit.sendwhatmsg(ph, msg, current_h, current_m + 2)
