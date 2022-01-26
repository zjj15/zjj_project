from autost.api import *
DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
## param name: keyname
## param range: ['itcommander','presetswitch','steeringcontrolswitch','keyevent','itcmd','igsw','wirecontrol']
## action: choose one key from according type list

#-------------------1,IT Commander[M-CAN] panel-------------------
# eg:keyevent(hardkey_name, panel='IT Commander', mode='CAN', channel=CANBUS_CH1)
hardkey_ITCommander=[
    ##IT Commander[M-CAN]
    AUDIO,
    MENU,
    MAP,
    BACK,
    #进入Navi
    OK,
    #Navi画面有效
    ZOOM_UP,
    UP_RIGHT,
    UP_LEFT,
    ZOOM_DOWN,
    LEFT,
    RIGHT,
    DOWN_LEFT,
    DOWN,
    DOWN_RIGHT,
    #Camera[E-Call]
    # CAMERA
]
#-------------------2,Preset Switch[M-CAN] panel-------------------
# eg:keyevent(DAY_NIGHT, panel='Preset Switch', duration=2.0, mode='CAN', channel=CANBUS_CH1)
# eg:keyevent(DAY_NIGHT, panel='Preset Switch', mode='CAN', channel=CANBUS_CH1)
hardkey_PresetSwitch=[
    # delete VOLUME_ON_OFF,for this button affect lastsource
    #VOLUME_ON_OFF,
    VOLUME_DOWN,
    VOLUME_UP,
    TUNE_DOWN,
    TUNE_UP,
    SEEK_DOWN,
    SEEK_UP,
    #长按
    # 'DAY_NIGHT_long',
    #短按
    DAY_NIGHT,
    # CAMERA
]
#-------------------3,Steering Control Switch[M-CAN] panel-------------------
# eg:keyevent(VOLUME_UP, panel='Steering Control Switch', mode='CAN', channel=CANBUS_CH1)
hardkey_SteeringControlSwitch=[
    VOLUME_UP,
    VOLUME_DOWN,
    BACK,
    SEEK_DOWN,
    SEEK_UP,
    VR,
    MENU_DOWN,
    OK,
    MENU_UP,
    RIGHT,
    LEFT,
    TEL
]
#-------------------4,KeyEvent ---------------
# eg:keyevent(AUDIO)
hardkey_KeyEvent=[
    AUDIO,
    HOME,
    NAVI,
    BACK,
    # CAMERA,
    # delete VOLUME_ON_OFF,for this button affect lastsource
    #VOLUME_ON_OFF,
    #VOLUME_ON_OFF,
    VOLUME_UP,
    VOLUME_DOWN
]
#-------------------5,Wire Control------------
# eg:keyevent(AUDIO)
hardkey_WireControl=[
    WIRECTR_VOL_UP,
    WIRECTR_VOL_DOWN,
    WIRECTR_TEL_ON,
    WIRECTR_TEL_OFF,
    WIRECTR_TRACK_UP,
    WIRECTR_TRACK_DOWN,
    WIRECTR_TALK,
    WIRECTR_TEL
]
#-------------------6,IT CMD------------------
# eg:keyevent(AUDIO)
hardkey_ITCMD=[
    ITCMD_AUDIO,
    ITCMD_MENU,
    ITCMD_MAP_VOICE,
    ITCMD_BACK,
    # ITCMD_CAMERA,
    ITCMD_OK,
    #Map画面有效
    ITCMD_TILT_UP_LEFT,
    ITCMD_TILT_LEFT,
    ITCMD_TILT_DOWN_LEFT,
    ITCMD_TILT_DOWN_RIGHT,
    ITCMD_TILT_RIGHT,
    ITCMD_TILT_UP_RIGHT,
    ITCMD_DIAL_RIGHT,
    ITCMD_TILT_UP,
    ITCMD_DIAL_LEFT,
    ITCMD_TILT_DOWN
]
#-------------------7,IG-SW-------------------
# eg:keyevent(AUDIO)
hardkey_IGSW=[
    PRESET_VOL_ENCODER,
    PRESET_VOL_LEFT,
    PRESET_VOL_RIGHT,
    # delete this key, for source switch
    # PRESET_AUDIO,
    PRESET_FOLDER_UP,
    PRESET_FOLDER_DOWN,
    PRESET_SEEK_UP,
    PRESET_SEEK_DOWN,
    #长按, duration=2.0
    # 'PRESET_DAY_NIGHT_long',
    PRESET_DAY_NIGHT,
    #PRESET_AVM_RVM
]

def press_key_onstart(key_type_name, key_name):
    print('key_type_name:%s, key_name:%s'%(key_type_name, key_name))
    if 'itcommander'== key_type_name:
        #hardkey_list = hardkey_ITCommander
        keyevent(key_name, panel='IT Commander', mode='CAN', channel=CANBUS_CH1)
    elif 'presetswitch' == key_type_name:
        #hardkey_list = hardkey_PresetSwitch
        if 'DAY_NIGHT_long' == key_name:
            keyevent(DAY_NIGHT, panel='Preset Switch', duration=2.0, mode='CAN', channel=CANBUS_CH1)
        else:
            keyevent(key_name, panel='Preset Switch', mode='CAN', channel=CANBUS_CH1)
    elif 'steeringcontrolswitch' == key_type_name:
        #hardkey_list = hardkey_SteeringControlSwitch
        keyevent(key_name, panel='Steering Control Switch', mode='CAN', channel=CANBUS_CH1)
    elif key_type_name in ['keyevent', 'itcmd', 'igsw', 'wirecontrol']:
        if 'PRESET_DAY_NIGHT_long' == key_name:
            keyevent(PRESET_DAY_NIGHT, duration=2.0)
        else:
            keyevent(key_name)
    else:
        error('keyevent error')

# 0,get_param
key_type_name = get_param('keyname')

# 1,等待adb device与ide连接
print("wait for device start")
uri='Gaea://127.0.0.1:5037/GFEDCBA0987654321'
device(uri).adb.wait_for_device(timeout=60)
print("wait for device end")
# 2,割入HardKey
print('key_type_name:',key_type_name)
if key_type_name is None:
    error('invalid param')
else:
    hardkey_list = None
    if 'itcommander'== key_type_name:
        hardkey_list = hardkey_ITCommander
    elif 'presetswitch' == key_type_name:
        hardkey_list = hardkey_PresetSwitch
    elif 'steeringcontrolswitch' == key_type_name:
        hardkey_list = hardkey_SteeringControlSwitch
    elif 'keyevent' == key_type_name:
        hardkey_list = hardkey_KeyEvent
    elif 'itcmd' == key_type_name:
        hardkey_list = hardkey_ITCMD
    elif 'igsw' == key_type_name:
        hardkey_list = hardkey_IGSW
    elif 'wirecontrol' == key_type_name:
        hardkey_list = hardkey_WireControl

    import random
    rand_idx = random.randint(0,len(hardkey_list)-1)
    print('rand_idx:',rand_idx)
    key_name = hardkey_list[rand_idx]
    print('hardkey_to_press:',key_name)

    for i in range(1, 20):
        print("try..",i)
        try:
            press_key_onstart(key_type_name, key_name)
            print("割入HardKey: %s succeed! " % key_name)
            sleep(5)
        except Exception as e:
            print(str(e))
            sleep(0.5)
            continue
        else:
            break
    else:
        print('割入HardKey failed')
