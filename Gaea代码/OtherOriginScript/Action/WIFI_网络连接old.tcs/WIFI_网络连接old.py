from autost.api import *
import AbsPath

from Common.InfraLibAPI import *

WIFIName = ExternalDynamicConfig_getExternalWIFIName()

print("__脚本名称: " + __file__)
#1, 车机联网
# WiFi_网络连接
if exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/statusbar_wifi_good_mark.png"), timeout=1, threshold=0.90) or exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/statusbar_wifi_great_mark.png"), timeout=1, threshold=0.90):
    pass
else:
    do_segment(Segment("../../../InfraLib/ExternalDevices/WIFI/Common/BackHomeView.tcs"))
    if not exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/statusbar_wifi_good_mark.png"), timeout=3, threshold=0.90) or exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/statusbar_wifi_great_mark.png"), timeout=3, threshold=0.90):
        do_segment(Segment("../../../InfraLib/ExternalDevices/WIFI/Screen/迁移到中控设定画面.tcs"))
        do_segment(Segment("../../../InfraLib/ExternalDevices/WIFI/Screen/进入Wi-Fi设定画面.tcs"))
        do_segment(Segment("../../../InfraLib/ExternalDevices/WIFI/Action/WiFi 设定为ON.tcs"))
        sleep(3)
        if exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/statusbar_wifi_good_mark.png"), timeout=3, threshold=0.90) or exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/statusbar_wifi_great_mark.png"), timeout=3, threshold=0.90):
            pass
        else:
            for i in range(4):
                '''
                if exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_signal_4.png"), timeout=2, threshold=0.95):
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_signal_4.png"), timeout=3, threshold=0.95)
                    sleep(3)
                    continue
                elif exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_signal_3.png"), timeout=2, threshold=0.95):
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_signal_3.png"), timeout=3, threshold=0.95)
                    sleep(3)
                    continue
                '''
                if poco(text='请输入“'+WIFIName+'”的密码').exists():
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_switchToNum.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    poco('完成', text='完成').click()
                    sleep(3)
                    wait_for_disappearance(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_连接中MSG.png"),timeout=60)
                    sleep(2) 
                elif poco('允许', text='允许', timeout=1).exists():
                    for _ in range(3):
                        if poco('允许', text='允许', timeout=1).exists():
                            poco('允许', text='允许').click()
                            sleep(0.5)
                    continue
                elif poco(text='讯飞车载输入法隐私政策', timeout=2).exists():
                    poco(text='不再提示').click()
                    sleep(1)
                    poco(text='同意').click()
                    touch([575,255])
                    continue
                elif poco('请输入“AP-16F-21”的密码', text='请输入“AP-16F-21”的密码', timeout=2).exists():
                    touch_if(Template("pic/输入框.png"),threshold=0.90,timeout=5.0)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_English_a.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_English_p.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_switchToNum.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_6.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_back.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_English_f.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_switchToNum.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_2.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_back.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_English_e.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_English_a.png"), timeout=2)
                    poco('完成', text='完成').click()
                    sleep(3)
                    wait_for_disappearance(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_连接中MSG.png"),timeout=60)
                    sleep(2)
                elif poco('请输入“AP-10F-07”的密码', text='请输入“AP-10F-07”的密码', timeout=2).exists():
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_switchToNum.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_2.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_0.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_9.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_2.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_0.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_2.png"), timeout=2)
                    poco('完成', text='完成').click()
                    sleep(3)
                    wait_for_disappearance(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_连接中MSG.png"),timeout=60)
                    sleep(2)
                elif poco('请输入“AP-16F-02”的密码', text='请输入“AP-16F-02”的密码', timeout=2).exists():
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_switchToNum.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_2.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_0.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_9.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_2.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_0.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_2.png"), timeout=2)
                    poco('完成', text='完成').click()
                    sleep(3)
                    wait_for_disappearance(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_连接中MSG.png"),timeout=60)
                    sleep(2)
                elif poco('请输入“AP_16F_Xiaomi”的密码', text='请输入“AP_16F_Xiaomi”的密码', timeout=2).exists():
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_switchToNum.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_2.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_0.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_9.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_0.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_2.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_0.png"), timeout=2)
                    poco('完成', text='完成').click()
                    sleep(3)
                    wait_for_disappearance(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_连接中MSG.png"),timeout=60)
                    sleep(2)
                elif poco('请输入“AutoTest_xm_1”的密码', text='请输入“AutoTest_xm_1”的密码', timeout=2).exists():
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_switchToNum.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_num_1.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_back.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_English_capital.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_English_upper_A.png"), timeout=2)
                    touch_if(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_English_lower.png"), timeout=2)
                    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/input_English_a.png"), timeout=2)
                    poco('完成', text='完成').click()
                    sleep(3)
                    wait_for_disappearance(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_连接中MSG.png"),timeout=60)
                    sleep(2)
                #elif poco(text='请输入“AP-16F-99”的密码').exists():
                else:
                    continue
                if exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/wifi_setting_已连接状态.png"), timeout=20):
                    break
if exists(Template("../../../InfraLib/ExternalDevices/WIFI/Design/加油智慧_仅仅路过btn.png"), timeout=1):
    touch(Template("../../../InfraLib/ExternalDevices/WIFI/Design/加油智慧_仅仅路过btn.png"), timeout=2)
