from autost.api import *
DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

sendCAN(METER_A104.ParkingBrakeStatus.phys, 2.0, interval=0.1, device=DEV1)
sendCAN(VDC_A9.VehicleSpeed.phys, 0.0, interval=0.1, device=DEV1)
