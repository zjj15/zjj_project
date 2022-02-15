from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

ST.current_source = 'current_source.png'
snapshot(rect=[254, 22, 52, 57], filename = os.path.join(ST.LOG_DIR, ST.current_source))


