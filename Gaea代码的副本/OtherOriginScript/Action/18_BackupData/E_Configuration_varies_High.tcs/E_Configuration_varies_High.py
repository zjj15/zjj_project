from autost.api import *

DEV1 = ST.DEV1

#Configuration varies

#P42Q_Hign -> P42Q_MidLow_optTC
do_segment(Segment("../../../Common/Switch_To_P42Q_MidLow_optTC.tcs"))

sleep(10)

#P42Q_MidLow_optTC -> P42Q_Hign
do_segment(Segment('../../../Common/Switch_To_P42Q_High.tcs'))
