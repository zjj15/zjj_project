from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

poco(ST.delete_program_1_name,text=ST.delete_program_1_name, timeout=1.5).assert_not_exists()