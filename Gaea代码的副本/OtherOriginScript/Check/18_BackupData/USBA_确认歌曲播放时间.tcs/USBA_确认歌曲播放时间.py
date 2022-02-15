from autost.api import *
import re

#车机重启后，有概率拿不到控件树，改用image_to_string接口
text_progress = None
for _ in range(5):
    text_progress = image_to_string([430, 527, 112, 34])
    #print(text_progress)
    res = re.match("[0-9]{2}:[0-9]{2}$",text_progress)
    if res:
       print('OK: ', text_progress)
       break
    else:
        print('NG: ', text_progress)

print('text_progress:', text_progress)
progress_startTo = '2021-5-1 '
if len(text_progress)>5:
    progress_startTo = time.strptime(progress_startTo + text_progress,'%Y-%m-%d %H:%M:%S')
else:
    progress_startTo = time.strptime(progress_startTo +' 00:' + text_progress,'%Y-%m-%d %H:%M:%S')

print("ST.usbaudio_playtime:", ST.usbaudio_playtime)
if len(ST.usbaudio_playtime)>5:
    usbaudio_playtime = time.strptime('2021-5-1 ' + ST.usbaudio_playtime,'%Y-%m-%d %H:%M:%S')
else:
    usbaudio_playtime = time.strptime('2021-5-1 ' +' 00:' + ST.usbaudio_playtime,'%Y-%m-%d %H:%M:%S')

time1= time.mktime(progress_startTo)
time2= time.mktime(usbaudio_playtime)
#time2= time.mktime(playtime_text)
time_diff = time1 - time2
print('time_diff:',time_diff)
if time_diff<35:
   pass
else:
    error('USB Auio Play time Keep Check Error!')