from autost.api import *
DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

#1.ACCOff
# C1A-HS OFF
sendCAN(BCM_A110.V_WakeUpSleepCommand.phys, 0.0, channel=CANBUS_CH2)
stopCAN(BCM_A112, channel=CANBUS_CH2)
stopCAN(BCM_A113, channel=CANBUS_CH2)
stopCAN("0x457.byte 3.phys", channel=CANBUS_CH2)
sleep(20)

# C1A-HS ON
sendCAN(BCM_A110.V_WakeUpSleepCommand.phys, 3.0, interval=0.1, channel=CANBUS_CH2)
sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1, channel=CANBUS_CH2)
sendCAN(BCM_A113.VehicleStates.phys, 5.0, interval=0.1, channel=CANBUS_CH2)
sendCAN("0x457.byte 3.phys", 1.0, frame_data=bytearray(b'\x00\x00\x00\x01\x00\x00\x00\x00'), is_frame=True, interval=0.1, frame_id=1111, channel=CANBUS_CH2)


