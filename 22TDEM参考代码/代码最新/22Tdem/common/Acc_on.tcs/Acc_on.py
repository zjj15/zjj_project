from autost.api import *
#import AbsPath


sendCAN(BCM_A110.V_WakeUpSleepCommand.phys, 3.0, interval=0.1)
sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1)
sendCAN(BCM_A113.VehicleStates.phys, 5.0, interval=0.1)
sendCAN("0x457.byte 3.phys", 1.0, interval=0.1, frame_id=1111, frame_data=bytearray(b'\x00\x00\x00\x01\x00\x00\x00\x00'), is_frame=True)
sleep(2)
