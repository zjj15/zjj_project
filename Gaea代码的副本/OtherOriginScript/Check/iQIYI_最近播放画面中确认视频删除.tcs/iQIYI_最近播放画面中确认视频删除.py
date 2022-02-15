from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

poco(className='android.widget.TextView', text=ST.delete_program_1_name, timeout=2).assert_not_exists()
