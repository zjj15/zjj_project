from autost.api import *

touch_if(Template('../../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=2)

touch_if(Template('../../../Design/OnlineVideo_Center.png'), timeout=2, threshold=0.93)

touch_if(Template('../../../Design/OnlieVideo_Setting_View_History.png'), timeout=2)

touch([311, 320])
for i in range(5):
    sleep(6)
    if exists(Template('../../../Design/OnlineVideo_Play_Bar.png'), timeout=1) or exists(Template('../../../Design/OnlineVideo_暂停btn.png'), timeout=1):
        break
    elif exists(Template('../../../Design/OnlineVideo_视频刷新.png'), timeout=1):
        touch(Template('../../../Design/OnlineVideo_视频刷新.png'), timeout=1)


playtime_text = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')

print("playtime_text = " + playtime_text)
progress_startTo = '2021-5-1 '
if len(playtime_text)>5:
    progress_startTo = time.strptime(progress_startTo + playtime_text,'%Y-%m-%d %H:%M:%S')
else:
    progress_startTo = time.strptime(progress_startTo +' 00:' + playtime_text,'%Y-%m-%d %H:%M:%S')

if len(ST.OnlineVideo_playtime)>5:
    #print("ST.OnlineVideo_playtime = " + ST.OnlineVideo_playtime)
    ST.OnlineVideo_playtime = time.strptime('2021-5-1 ' + ST.OnlineVideo_playtime,'%Y-%m-%d %H:%M:%S')
else:
    ST.OnlineVideo_playtime = time.strptime('2021-5-1 ' +' 00:' + ST.OnlineVideo_playtime,'%Y-%m-%d %H:%M:%S')

time1= time.mktime(progress_startTo)
time2= time.mktime(ST.OnlineVideo_playtime)
time_diff = time1 - time2
print('time_diff:',time_diff)
if time_diff<5:
   pass
else:
    error('OnlineVideo Play Time Check Error!')
