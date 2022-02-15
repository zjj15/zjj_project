from autost.api import *

uri='Gaea://127.0.0.1:5037/GFEDCBA0987654321'
process_name = get_param('procname')

def action():
    try:
        device(uri).adb.cmd("root")
        #sleep(1)
        process_id = shell("pidof %s" % process_name)
        print("found process_id:%s    start killing..."%process_id)
        shell("kill -9 `pidof %s`" % process_name)
        print('kill succeed!')
        sleep(1)
        process_id_after_kill = shell("pidof %s" % process_name)
        print('process_id_after_kill:%s' % process_id_after_kill)
    except:
        print("process:%s not found..." % process_name)


if process_name is None:
    error('invalid param')
else:
    action()
