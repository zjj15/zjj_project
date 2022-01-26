from autost.api import *
dict_Phone_step ={
    1: ST.Phone_Volume_step1_Point,
    10: ST.Phone_Volume_step10_Point,
    11: ST.Phone_Volume_step11_Point,
    12: ST.Phone_Volume_step12_Point,
    13: ST.Phone_Volume_step13_Point,
    14: ST.Phone_Volume_step14_Point,
    15: ST.Phone_Volume_step15_Point,
    16: ST.Phone_Volume_step16_Point,
    17: ST.Phone_Volume_step17_Point,
    18: ST.Phone_Volume_step18_Point,
    19: ST.Phone_Volume_step19_Point,
    2: ST.Phone_Volume_step2_Point,
    20: ST.Phone_Volume_step20_Point,
    21: ST.Phone_Volume_step21_Point,
    22: ST.Phone_Volume_step22_Point,
    23: ST.Phone_Volume_step23_Point,
    24: ST.Phone_Volume_step24_Point,
    25: ST.Phone_Volume_step25_Point,
    26: ST.Phone_Volume_step26_Point,
    27: ST.Phone_Volume_step27_Point,
    28: ST.Phone_Volume_step28_Point,
    29: ST.Phone_Volume_step29_Point,
    3: ST.Phone_Volume_step3_Point,
    30: ST.Phone_Volume_step30_Point,
    31: ST.Phone_Volume_step31_Point,
    4: ST.Phone_Volume_step4_Point,
    5: ST.Phone_Volume_step5_Point,
    6: ST.Phone_Volume_step6_Point,
    7: ST.Phone_Volume_step7_Point,
    8: ST.Phone_Volume_step8_Point,
    9: ST.Phone_Volume_step9_Point
}
DEV1 = ST.DEV1
phone_step = get_param('step')
if None == phone_step:
    print('phone_step is needed!')

#Item Action：设定多媒体音量[X]
print('Item Action：设定多媒体音量[step%s]' % phone_step)
try:
    if exists(Template('../../../Design/Phone_Volume_Title.png'), device=DEV1, timeout=4):
        touch(dict_Phone_step[phone_step],device=DEV1)
    assert_exists(Template('../../../Design/check_VS_Phone_Volume_%s.png' % phone_step), device=DEV1, timeout=4)

except:
    error('Slices/Phone_step step:%s setting error' % phone_step)
