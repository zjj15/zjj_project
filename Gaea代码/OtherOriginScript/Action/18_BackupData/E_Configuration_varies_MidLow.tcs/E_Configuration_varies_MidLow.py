from autost.api import *

DEV1 = ST.DEV1

#Configuration varies

#P42Q_MidLow_optTC -> P42Q_MidLow_optC
do_segment(Segment('../../../Common/Switch_To_P42Q_MidLow_optC.tcs'))

sleep(10)

#P42Q_MidLow_optC -> P42Q_MidLow_optTC
do_segment(Segment('../../../Common/Switch_To_P42Q_MidLow_optTC.tcs'))

