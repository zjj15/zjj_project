from autost.api import *

DEV1 = ST.DEV1
##BackUpData 共通前置条件设定

# pkb on
sendCAN(METER_A104.ParkingBrakeStatus.phys, 2.0, interval=0.1, device=DEV1)
sleep(1)
