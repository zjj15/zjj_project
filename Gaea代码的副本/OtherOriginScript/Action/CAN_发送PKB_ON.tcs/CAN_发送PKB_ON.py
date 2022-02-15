from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
# PKB ON
sendCAN(BCM_A113.VehicleStates.phys, 0.0, interval=0.1)
sendCAN(METER_A104.ParkingBrakeStatus.phys, 2.0, interval=0.1, channel=CANBUS_CH2)
sleep(2)