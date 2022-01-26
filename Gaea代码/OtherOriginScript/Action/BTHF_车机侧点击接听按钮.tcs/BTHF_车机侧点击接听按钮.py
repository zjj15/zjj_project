from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

#BTHF_Incoming_Screen
for i in range(10):
    if exists(Template('../../Design/BTHF_Incoming_Screen.png'), timeout=1):
        touch_in(Template('../../Design/BTHF_Incoming_ok.png'), Template('../../Design/BTHF_Incoming_Screen.png'), timeout=2, device=DEV1)
    if exists(Template('../../Design/BTHF_base_incoming_.png')):
        touch_in(Template('../../Design/BTHF_base_Incoming_ok.png'), Template('../../Design/BTHF_base_incoming_.png'))
    if exists(Template('../../Design/BTHF_Outgoing_Screen.png'), timeout=1):
        break
    if exists(Template('../../Design/BTHF_Outing_HangUp.png'), timeout=1):
        break
    if exists(Template('../../Design/BTHF_statusbar_EndCallBtn.png'), timeout=1):
        break
    if exists(Template('../../Design/BTHF_EndCallBtn.png'), timeout=1):
        break
else:
    error('接听电话 error')