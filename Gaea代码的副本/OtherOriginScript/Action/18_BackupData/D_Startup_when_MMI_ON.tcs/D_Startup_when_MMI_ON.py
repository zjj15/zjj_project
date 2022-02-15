from autost.api import *
# When B+ ON, the data is saved at the last C1A-HS OFF STATE

DEV1 = ST.DEV1

#B+ OFF
##ON STATE ->  MMI OFF STATE 
###VehicleStates = OFF && ProbableCustomerFeedBackNeed = Customer feedback probably not needed except E-CALL(Manual or ACN) mode
stopCAN(BCM_A113.VehicleStates.phys, 0.0, interval=0.1, device=DEV1)
stopCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 0.0, interval=0.1, device=DEV1)

###Max100ms
sleep(6)

##MMI OFF STATE ->  ON STATE
sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1, device=DEV1)
sendCAN(BCM_A113.VehicleStates.phys, 5, interval=0.1, device=DEV1)
sendCAN("0x457.byte 3.phys", 1.0, interval=0.1, frame_id=1111, frame_data=bytearray(b'\x00\x00\x00\x01\x00\x00\x00\x00'), is_frame=True)

#sleep(30)
