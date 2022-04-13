import pywhatkit
import time
from datetime import datetime

def send_sms(msg,ph):
    t = time.localtime()
    current_h = int(time.strftime("%H", t))
    current_m = int(time.strftime("%M", t))
    pywhatkit.sendwhatmsg(ph, msg, current_h, current_m + 1)