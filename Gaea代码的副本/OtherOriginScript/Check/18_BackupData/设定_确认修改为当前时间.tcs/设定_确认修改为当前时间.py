from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

# confirm time changed success

#assert_exists(Template(os.path.join(ST.LOG_DIR, ST.changed_time_1)),device=DEV1)
# 获取当前时间
currentTime_H = int(poco(pos2=[675, 435]).get_attr('text'))
currentTime_M = int(poco(pos2=[854, 435]).get_attr('text'))

if currentTime_H == ST.CurrentTime_H:
    diff = currentTime_M - ST.CurrentTime_M
elif 1 == (currentTime_H - ST.CurrentTime_H):
    diff = currentTime_M + 60 - ST.CurrentTime_M
elif -23 == (currentTime_H - ST.CurrentTime_H):
    diff = currentTime_M + 60 - ST.CurrentTime_M
else:
    error('check current time[H] changed error!') 
print('check current time[diff]:',diff)
if 5 > diff:
    pass
else:
    error('check current time[M] changed error!') 
assert_exists(Template(os.path.join(ST.LOG_DIR, ST.changed_time_2)),device=DEV1)

