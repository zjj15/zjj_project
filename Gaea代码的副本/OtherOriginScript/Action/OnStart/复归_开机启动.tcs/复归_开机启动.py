from autost.api import *

try:
    keyevent(ITCMD_MENU)
    assert_exists(Template('../../../Design/Statusbar_Navi_0.png'), timeout=1)
except:
    # OFF STATE
    bup_off()
    sleep(1)
    bup_on()
    sleep(3)
    # C1A-HS ON
    sendCAN(BCM_A110.V_WakeUpSleepCommand.phys, 3.0, interval=0.1, channel=CANBUS_CH2)
    sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1, channel=CANBUS_CH2)
    sendCAN(BCM_A113.VehicleStates.phys, 5.0, interval=0.1, channel=CANBUS_CH2)
    sendCAN("0x457.byte 3.phys", 1.0, frame_data=bytearray(b'\x00\x00\x00\x01\x00\x00\x00\x00'), frame_id=1111, interval=0.1, is_frame=True, channel=CANBUS_CH2)
    #2.Check车机启动
    sleep(20)
    assert_exists(Template('../../../Design/Statusbar_Navi_0.png'), timeout=30)

