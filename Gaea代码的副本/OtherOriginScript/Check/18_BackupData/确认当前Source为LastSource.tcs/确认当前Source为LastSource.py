from autost.api import *

do_segment(Segment('../../../Common/BackHomeView.tcs'))

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.current_source)))
except:
    error('Last Source Check K Error!')