from autost.api import *

###机型：P42Q High
###外设：Bose Amp
dict_media_volume_step = {
    0: ST.Media_Volume_step0_Point,
    1: ST.Media_Volume_step1_Point,
    10: ST.Media_Volume_step10_Point,
    11: ST.Media_Volume_step11_Point,
    12: ST.Media_Volume_step12_Point,
    13: ST.Media_Volume_step13_Point,
    14: ST.Media_Volume_step14_Point,
    15: ST.Media_Volume_step15_Point,
    16: ST.Media_Volume_step16_Point,
    17: ST.Media_Volume_step17_Point,
    18: ST.Media_Volume_step18_Point,
    19: ST.Media_Volume_step19_Point,
    2: ST.Media_Volume_step2_Point,
    20: ST.Media_Volume_step20_Point,
    21: ST.Media_Volume_step21_Point,
    22: ST.Media_Volume_step22_Point,
    23: ST.Media_Volume_step23_Point,
    24: ST.Media_Volume_step24_Point,
    25: ST.Media_Volume_step25_Point,
    26: ST.Media_Volume_step26_Point,
    27: ST.Media_Volume_step27_Point,
    28: ST.Media_Volume_step28_Point,
    29: ST.Media_Volume_step29_Point,
    3: ST.Media_Volume_step3_Point,
    30: ST.Media_Volume_step30_Point,
    31: ST.Media_Volume_step31_Point,
    32: ST.Media_Volume_step32_Point,
    33: ST.Media_Volume_step33_Point,
    34: ST.Media_Volume_step34_Point,
    35: ST.Media_Volume_step35_Point,
    36: ST.Media_Volume_step36_Point,
    37: ST.Media_Volume_step37_Point,
    38: ST.Media_Volume_step38_Point,
    39: ST.Media_Volume_step39_Point,
    4: ST.Media_Volume_step4_Point,
    40: ST.Media_Volume_step40_Point,
    5: ST.Media_Volume_step5_Point,
    6: ST.Media_Volume_step6_Point,
    7: ST.Media_Volume_step7_Point,
    8: ST.Media_Volume_step8_Point,
    9: ST.Media_Volume_step9_Point
}
DEV1 = ST.DEV1
media_step = get_param('step')
if None == media_step:
    print('media_step is needed!')
#Item Action：设定多媒体音量[stepX]
print('Item Action：设定多媒体音量[step%s]' % media_step)
try:
    if(exists(Template('../../../../Design/Media_Volume_Tiltle.png'),device=DEV1, timeout=4)):
        touch(dict_media_volume_step[media_step],device=DEV1)
        touch(dict_media_volume_step[media_step],device=DEV1)
        touch(dict_media_volume_step[media_step],device=DEV1)
        touch(dict_media_volume_step[media_step],device=DEV1)
    assert_exists(Template("../../../../Design/check_media_volume_step%s.png" % media_step),device=DEV1, timeout=4)

except:
    error('[P42Q_High] Slices/Media_step step:%s setting error' % media_step)
