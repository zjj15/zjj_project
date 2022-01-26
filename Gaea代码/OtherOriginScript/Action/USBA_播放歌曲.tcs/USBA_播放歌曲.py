from autost.api import *
import re
'''
touch_if(Template('../../Design/USBAudio_PauseButton.png'), timeout=2)

try:
    assert_exists(Template('../../Design/USBAudio_PlayBar.png'))
except:
    error('USB Audio Play Error!s')

#touch(Template('../../Design/USBAudio_PlayButton.png'))

#ST.usbaudio_playtime = 'usbaudio_playtime.png'
#snapshot(rect=[467, 528, 84, 33], filename=os.path.join(ST.LOG_DIR, ST.usbaudio_playtime))

#车机重启后，有概率拿不到控件树，改用image_to_string接口
playtime_text = None
for _ in range(10):
    playtime_text = image_to_string([430, 527, 112, 34])
    res = re.match("[0-9]{2}:[0-9]{2}$",playtime_text)
    if res:
       print('OK: ', playtime_text)
       break
    else:
        print('NG: ', playtime_text)

date = '2021-5-1'

if len(playtime_text)>5:
    ST.usbaudio_playtime_text = time.strptime(date + playtime_text,'%Y-%m-%d %H:%M:%S')
else:
    ST.usbaudio_playtime_text = time.strptime(date +' 00:' + playtime_text,'%Y-%m-%d %H:%M:%S')

print('ST.USBAudio playtime :',ST.usbaudio_playtime_text)
'''
sleep(5)
playtime_text = image_to_string([430, 527, 112, 34])
ST.usbaudio_playtime = image_to_string([430, 527, 112, 34])
print("ST.usbaudio_playtime = " + ST.usbaudio_playtime)