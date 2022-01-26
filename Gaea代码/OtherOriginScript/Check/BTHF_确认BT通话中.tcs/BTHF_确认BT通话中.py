from autost.api import * 

print('__脚本名称: ' + __file__)


CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

if exists(Template("../../Design/BTHF_Outgoing_Screen.png"), timeout=1):
    pass
elif exists(Template("../../Design/BTHF_Outing_HangUp.png"), timeout=1):
    pass
elif exists(Template("../../Design/BTHF_statusbar_EndCallBtn.png"), timeout=1):
    pass
elif exists(Template("../../Design/BTHF_EndCallBtn.png"), timeout=1):
    pass
else:
    error('BTHF_calling Error!')