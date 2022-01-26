from autost.api import *
# When B+ ON, the data is saved at the last C1A-HS OFF STATE

DEV1 = ST.DEV1

#B+ OFF
##ON STATE ->  MMI OFF STATE 
###VehicleStates = OFF && ProbableCustomerFeedBackNeed = Customer feedback probably not needed except E-CALL(Manual or ACN) mode
stopCAN(BCM_A113.VehicleStates.phys, 0.0, interval=0.1, device=DEV1)
stopCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 0.0, interval=0.1, device=DEV1)

###Max100ms
sleep(1)

##MMI OFF STATE -> OFF STATE
###V_WakeUpSleepCommand = Go to Sleep
stopCAN(BCM_A110.V_WakeUpSleepCommand.phys, 0.0, interval=0.1, device=DEV1)

###Max 4sec
sleep(5)

#B+off -> on
bup_off()
sleep(40)
bup_on()

#冷启动
##OFF STATE ->  MMI OFF STATE 
sendCAN(BCM_A110.V_WakeUpSleepCommand.phys, 3, BCM_A110.V_WakeUpType.phys, 0, interval=0.1, device=DEV1)
#sendCAN(BCM_A113.DeliveryModeInformation_v2.phys, 0, interval=0.1, device=DEV1)

##Max 4sec
sleep(5)

##MMI OFF STATE ->  ON STATE
sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1, device=DEV1)
sendCAN(BCM_A113.VehicleStates.phys, 5, interval=0.1, device=DEV1)
sendCAN("0x457.byte 3.phys", 1.0, interval=0.1, frame_id=1111, frame_data=bytearray(b'\x00\x00\x00\x01\x00\x00\x00\x00'), is_frame=True)

sleep(30)

