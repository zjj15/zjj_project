from autost.api import *
DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
## param name: process_name
## param range: android, 3rdApp, package, hal, framework
## action: choose one process from according type list

uri='Gaea://127.0.0.1:5037/GFEDCBA0987654321'
# iAuto进程列表
# process_type_所属Layer
process_type_3rdApp=[
    'cn.kuwo.kwmusiccar',##check is exists
    'com.autonavi.amapauto',
    'com.changba.sd',
    'com.szlanyou.usercenter',
    'com.szlanyou.dasmarthome2',
    'com.iflytek.inputmethod',
    'com.iflytek.cutefly.speechclient.hmi'
]
process_type_package=[
    'com.iauto.diag',##check is exists
    # 车机重启后touch失效    
    #'com.android.systemui',
    'com.iauto.av',
    'com.iauto.home',
    'com.iauto.phone',
    'com.iauto.setting',
    'com.iauto.voicerecognition',
    'com.iauto.systemview',
    'com.iauto.onlinevideo'
]
process_type_HAL = [
    #'vehicle',#vehicle与comd合并, vehicle进程不存在了
    'comd',
    #'sysd',#车机重启很久
    # delete this process: for source switch
    # 'connectserver',
    'ethernetd',
    'dtlogd',
    'rtapd',
    'lightd',
    'resourced',
    'camerad'
]
process_type_framework = [
    'diagserver',
    'iapserver',
    'meterserver',
    'dataserver',
    'dcmserver',
    'mediamanager',
    'carnetserver',
    'com.iauto.cameraserver',
    #'com.iauto.mediaserver',#kill该进程lastsource可能不能复归
    'com.iauto.miscserver',
    # delete: for source switch    
    # 'com.iauto.systemserver',
    'com.iauto.csagent',
    'com.iauto.naviclient'
]
# Android原生Framework&Native进程列表
# process_type_所属
process_type_android = [
    'init',
    'ueventd',
    'logd',
    'vpud',
    # 'servicemanager',
    'hwservicemanager',
    'vndservicemanager',
    'mcDriverDaemon',
    'android.hardware.keymaster@3.0-service',
    # BugID #825396
    #'vold',
    # delete: for source switch
    # 'netd',
    # 'zygote64',
    # kill this process lead to partial restart of ivi which make checking last source unavilable
    # run_id=44952, case_run_id=13048756
    #'zygote',
    'iptables-restore',
    'ip6tables-restore',
    'android.hidl.allocator@1.0-service',
    'android.hardware.bluetooth@1.0-service',#BT重连需要1min
    #'android.hardware.broadcastradio@1.1-service',
    #'android.hardware.cas@1.0-service',
    #'android.hardware.drm@1.0-service',
    #'android.hardware.gatekeeper@1.0-service',
    # delete: for source switch
    # 'android.hardware.graphics.allocator@2.0-service',
    #'android.hardware.graphics.composer@2.1-service',
    #'android.hardware.light@2.0-service',
    #'android.hardware.memtrack@1.0-service',
    #'android.hardware.sensors@1.0-service',
    'android.hardware.thermal@1.0-service',
    'android.hardware.wifi@1.0-service',
    'lmkd',
    #'surfaceflinger',#车机有概率黑屏
    'thermalserviced',
    #'system_server',
    'mnld',
    'audioserver',
    'cameraserver',
    'drmserver',
    'installd',
    'keystore',
    'mediadrmserver',
    'media.extractor',
    'mediaserver',
    'storaged',
    'wificond',
    'media.codec',
    'gatekeeperd',
    'tombstoned',
    #'com.android.systemui',
    'com.android.car',
    'com.android.packageinstaller'
]

spec_proc_list = [
    # process_type_android
    # 'servicemanager',
    'hwservicemanager',
    # delete: for source switch
    # 'netd',
    # 'zygote64',
    'zygote',
    # 'system_server',
    'surfaceflinger',
    # delete: for source switch
    # 'android.hardware.graphics.allocator@2.0-service',
    #'android.hardware.graphics.composer@2.1-service',
    #'android.hardware.sensors@1.0-service',
    'comd'
]
import time
def print_time():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

## wait the process restart
def sleep_after_kill_process():
    print_time()
    sleep(20)
    for _ in range(10):
        try:
            if exists(Template('../../../Design/Home_mark_focus.png'), timeout=20):
                print_time()
                sleep(5)
                break
            else:
                sleep(1)
        except Exception as e:
            print(str(e))
            sleep(0.5)
            continue

## ref:do_segment(Segment('../../kill_process_procname.tcs'),procname=process_name)
def action(process_to_kill):
    try:
        device(uri).adb.cmd("root")
        #sleep(1)
        for _ in range(3):
            try: 
                shell("ps -A | grep %s" % process_to_kill)
                break
            except:
                sleep(10)
        process_id = shell("pidof %s" % process_to_kill)
        print("found process_id:%s    start killing..."%process_id)
        shell("kill -9 `pidof %s`" % process_to_kill)
        print('kill succeed!')
        sleep(1)
        process_id_after_kill = shell("pidof %s" % process_to_kill)
        print('process_id_after_kill:%s' % process_id_after_kill)
        ## for special case
        if process_to_kill in spec_proc_list:
            sleep_after_kill_process()
    except:
        print("process:%s not found..." % process_to_kill)
        ## for special case
        if process_to_kill in spec_proc_list:
            sleep_after_kill_process()

# 0,get_param
process_name = get_param('procname')

# 1,等待adb device与ide连接
print("wait for device start")
device(uri).adb.wait_for_device(timeout=60)
print("wait for device end")
# 2,kill process
if process_name is None:
    error('invalid param')
else:
    process_list = None
    if 'android'==process_name:
        process_list = process_type_android
    elif 'package' == process_name:
        process_list = process_type_package
    elif 'hal' == process_name:
        process_list = process_type_HAL
    elif '3rdApp' == process_name:
        process_list = process_type_3rdApp
    elif 'framework' == process_name:
        process_list = process_type_framework

    import random
    rand_idx = random.randint(0,len(process_list)-1)
    print('rand_idx:',rand_idx)
    process_to_kill = process_list[rand_idx]
    print('process_to_kill:',process_to_kill)
    action(process_to_kill)
