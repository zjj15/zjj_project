from autost.api import *

if exists(Template("../../Design/KTV_录制中.png"), timeout=3):
    touch(Template("../../Design/KTV_录制中.png"), timeout=3)

if poco('录音关闭', text='录音关闭').exists():
    poco(text='录音关闭').click()